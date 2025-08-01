# smart-poop-bucket
Smart 3D printer poop bucket suitable for the Bambu A1. Track your poop with the web interface.

Why did I create this? Well, simply put, I hate the waste produced by multicolour prints. I like to minimise my waste when printing, and also when I sell my multicolour prints I need to calculate the price by including the weight of the poop and the printed objects. So, I thought it would be really handy, rather than me having to empty my poop bin and weigh it myself every time, instead have a smart poop bin where I can keep track of the poop weight of each print, without having to go through the hassle of weighing it myself.


```

Wiring diagram:

             ┌──────────────────────────────────────────────┐
             │             ESP32-S3 DevKitC-1               │
             │                                              │
             │ GPIO4 ────────► DT (HX711)                   │
             │ GPIO5 ────────► SCK (HX711)                  │
             │ 3V3   ────────► VCC (HX711)                  │
             │ GND   ────────► GND (HX711)                  │
             └──────────────────────────────────────────────┘


             ┌──────────────────────────────────────────────┐
             │                  HX711 Module                │
             │                                              │
             │ VCC   ◄─────── 3V3 (ESP32-S3)                │
             │ GND   ◄─────── GND (ESP32-S3)                │
             │ DT    ◄─────── GPIO4 (ESP32-S3)              │
             │ SCK   ◄─────── GPIO5 (ESP32-S3)              │
             │ E+    ◄─────── Red wire (Load Cell)          │
             │ E-    ◄─────── Black wire (Load Cell)        │
             │ A+    ◄─────── White wire (Load Cell)        │
             │ A-    ◄─────── Green wire (Load Cell)        │
             └──────────────────────────────────────────────┘


             ┌──────────────────────────────────────────────┐
             │                50kg Load Cell                │
             │                                              │
             │ Red   ───────► E+ (HX711)                    │
             │ Black ───────► E- (HX711)                    │
             │ White ───────► A+ (HX711)                    │
             │ Green ───────► A- (HX711)                    │
             └──────────────────────────────────────────────┘



```
