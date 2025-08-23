import network
import socket
import time
import machine
import json
import os
from machine import Pin
from hx711 import HX711      # robert-hh hx711_gpio variant saved as hx711.py

PIN_DOUT = 16
PIN_SCK  = 17

pin_dout = Pin(PIN_DOUT, Pin.IN, pull=Pin.PULL_DOWN)
pin_sck  = Pin(PIN_SCK, Pin.OUT)

hx = HX711(pin_sck, pin_dout)

print(">>> main.py is running!")

CALFILE = "calib.json"

def load_calibration():
    if CALFILE in os.listdir():
        try:
            with open(CALFILE, "r") as f:
                cal = json.load(f)
            if "offset" in cal:
                try:
                    hx.set_offset(int(cal["offset"]))
                except Exception:
                    pass
            if "scale" in cal:
                try:
                    hx.set_scale(float(cal["scale"]))
                except Exception:
                    pass
            return cal
        except Exception:
            return None
    return None

def save_calibration(offset=None, scale=None):
    cal = {}
    if CALFILE in os.listdir():
        try:
            with open(CALFILE, "r") as f:
                cal = json.load(f)
        except Exception:
            cal = {}
    if offset is not None:
        cal["offset"] = int(offset)
    if scale is not None:
        cal["scale"] = float(scale)
    with open(CALFILE, "w") as f:
        json.dump(cal, f)

load_calibration()

SSID = 'VM9482679'
PASSWORD = 'oombSohukdcPek3i'

def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    if not wlan.isconnected():
        wlan.connect(SSID, PASSWORD)
        print("Connecting to WiFi...")
        while not wlan.isconnected():
            time.sleep(1)
    print('Connected to WiFi:', wlan.ifconfig())

HFILE = "poop_log.json"
def load_history():
    try:
        with open(HFILE, "r") as f:
            return json.load(f)
    except:
        return []

def save_history(history):
    with open(HFILE, "w") as f:
        json.dump(history, f)

history = load_history()
current_start_weight = None

def safe_raw_read(avg=5):
    try:
        return hx.read_average(avg)
    except Exception:
        return hx.read()

def safe_units_read(avg=5):
    try:
        return hx.get_units()
    except Exception:
        return safe_raw_read(avg)

def send_headers(cl, content_type="text/html"):
    cl.send('HTTP/1.0 200 OK\nAccess-Control-Allow-Origin: *\nContent-Type: {}\n\n'.format(content_type))

def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        request = cl.recv(2048).decode()
        if 'favicon' in request:
            cl.close()
            continue

        path = "/"
        try:
            first_line = request.split("\n")[0]
            parts = first_line.split(" ")
            if len(parts) >= 2:
                path = parts[1]
        except:
            pass

        response = ""
        if path.startswith("/start"):
            global current_start_weight
            current_start_weight = safe_units_read()
            response = "Started: {}".format(current_start_weight)
            send_headers(cl)
            cl.send(response)
            cl.close()
        elif path.startswith("/end"):
            end_weight = safe_units_read()
            delta = None
            if current_start_weight is not None:
                try:
                    delta = end_weight - current_start_weight
                except Exception:
                    delta = 0
            session = {
                "delta": delta,
                "start": current_start_weight,
                "end": end_weight,
                "timestamp": time.time(),
            }
            history.append(session)
            save_history(history)
            current_start_weight = None
            response = "Ended: {}".format(session)
            send_headers(cl)
            cl.send(response)
            cl.close()
        elif path.startswith("/clear"):
            history.clear()
            save_history(history)
            response = "Cleared"
            send_headers(cl)
            cl.send(response)
            cl.close()
        elif path.startswith("/data"):
            send_headers(cl, content_type="application/json")
            cl.send(json.dumps(history))
            cl.close()
        elif path.startswith("/tare"):
            time.sleep(0.1)
            offset = safe_raw_read(avg=15)
            try:
                hx.set_offset(int(offset))
            except AttributeError:
                try:
                    hx.tare()
                    offset = hx.read_average(15)
                except Exception:
                    pass
            save_calibration(offset=int(offset))
            response = "Tared (offset saved): {}".format(int(offset))
            send_headers(cl)
            cl.send(response)
            cl.close()
        elif path.startswith("/calibrate"):
            try:
                q = path.split("?",1)[1]
                params = {}
                for kv in q.split("&"):
                    if "=" in kv:
                        k,v = kv.split("=",1)
                        params[k]=v
                if "w" in params:
                    known_weight = float(params["w"])
                    raw = safe_raw_read(avg=15)
                    try:
                        off = None
                        val = hx.get_value()
                        diff = val
                    except Exception:
                        cal = None
                        try:
                            with open(CALFILE, "r") as f:
                                cal = json.load(f)
                            off = int(cal.get("offset", 0)) if cal else 0
                        except:
                            off = 0
                        diff = raw - off
                    if diff == 0:
                        response = "Error: difference is zero; ensure weight is on scale and offset is set (use /tare first)."
                    else:
                        scale = diff / known_weight
                        try:
                            hx.set_scale(scale)
                        except Exception:
                            pass
                        save_calibration(scale=scale)
                        response = "Calibrated: scale={} (raw/gram)".format(scale)
                else:
                    response = "Provide weight via ?w=GRAMS"
            except Exception as e:
                response = "Calibration error: {}".format(e)
            send_headers(cl)
            cl.send(response)
            cl.close()
        else:
            response = "<html><body><h1>HX711 ESP32</h1><p>Endpoints: /start /end /tare /calibrate?w=GRAMS /data /clear</p></body></html>"
            send_headers(cl)
            cl.send(response)
            cl.close()

import _thread

def print_loop():
    while True:
        try:
            val = safe_raw_read(avg=5)
            print("Raw:", val)
        except Exception as e:
            print("HX711 read error:", e)
        time.sleep(0.2)

_thread.start_new_thread(print_loop, ())

connect_wifi()
start_server()