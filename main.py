import network
import socket
import time
import machine
import json
import os
from hx711 import HX711  # Load the HX711 library for interfacing with the load cell

# Replace with your own WiFi credentials
SSID = 'YOUR_SSID'
PASSWORD = 'YOUR_PASSWORD'

# Set up the HX711 Load Cell (pin assignments: DT -> GPIO14, SCK -> GPIO15)
hx711 = HX711(dout=14, pd_sck=15)

# Connect to Wi-Fi
def connect_wifi():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(SSID, PASSWORD)
    print("Connecting to WiFi...")
    while not wlan.isconnected():
        time.sleep(1)
    print('Connected to WiFi:', wlan.ifconfig())

# Load history from file
def load_history():
    try:
        with open("poop_log.json", "r") as f:
            return json.load(f)
    except:
        return []

# Save history to file
def save_history(history):
    with open("poop_log.json", "w") as f:
        json.dump(history, f)

# Global variables for session tracking
history = load_history()
current_start_weight = None

# Start web server to handle requests
def start_server():
    addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
    s = socket.socket()
    s.bind(addr)
    s.listen(1)
    print('Listening on', addr)

    while True:
        cl, addr = s.accept()
        request = cl.recv(1024).decode()
        if 'favicon' in request:
            cl.close()
            continue

        response = ""
        if "/start" in request:
            global current_start_weight
            current_start_weight = hx711.read()  # Read the initial weight from the load cell
            response = "Started"
        elif "/end" in request:
            end_weight = hx711.read()  # Read the final weight after session ends
            delta = end_weight - current_start_weight if current_start_weight else 0
            session = {
                "delta": delta,
                "start": current_start_weight,
                "end": end_weight,
                "timestamp": time.time(),
                "weight": round(delta * 0.1, 2)  # Example: Conversion to kg or lb
            }
            history.append(session)
            save_history(history)
            current_start_weight = None
            response = "Ended"
        elif "/clear" in request:
            history.clear()
            save_history(history)
            response = "Cleared"
        elif "/data" in request:
            cl.send('HTTP/1.0 200 OK\nContent-Type: application/json\n\n')
            cl.send(json.dumps(history))
            cl.close()
            continue
        else:
            with open("index.html", "r") as f:
                response = f.read()

        cl.send('HTTP/1.0 200 OK\nContent-Type: text/html\n\n')
        cl.send(response)
        cl.close()

# Connect to Wi-Fi and start the web server
connect_wifi()
start_server()
