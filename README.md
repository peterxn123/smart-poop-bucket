# smart-poop-bucket
Smart 3D printer poop bucket suitable for the Bambu A1. Track your poop with the web interface.

Why did I create this? Well, simply put, I hate the waste produced by multicolour prints. I like to minimise my waste when printing, and also when I sell my multicolour prints I need to calculate the price by including the weight of the poop and the printed objects. So, I thought it would be really handy, rather than me having to empty my poop bin and weigh it myself every time, instead have a smart poop bin where I can keep track of the poop weight of each print, without having to go through the hassle of weighing it myself.

<img width="776" height="581" alt="image" src="https://github.com/user-attachments/assets/6c5cdaee-a8d4-4fe8-ae9d-04b7a8a23517" />

<img width="710" height="566" alt="image" src="https://github.com/user-attachments/assets/7649f82e-fafe-42af-ba1e-b64330573749" />


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


BOM:

| Quantity | Component                            | Model / Description                                         | Amazon UK Link                                                                                                                        | Notes                                     |
|----------|--------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| 1        | ESP32-S3                             | Generic ESP32-S3 devboard.                                  | [Link to ESP32-S3](https://www.amazon.co.uk/ESP32-DevKitC-WROOM1-Development-Bluetooth/dp/B0CLD4QKT1/ref=sr_1_5?crid=3S33M23LFOW3P)        | Main MCU with Wi-Fi + USB-C               |
| 1        | HX711 Load Cell Amplifier + 50KG     | HX711 24-bit ADC module bundled with 50kg load cells.       | [Link to HX711 Load Cell](https://www.amazon.co.uk/Weighting-Half-bridge-Amplifier-Bathroom-Arduino/dp/B07FMN1DBN/ref=sr_1_45)           | Amplifies load cell signal               |
| 40       | Jumper Wires (male–female)           | Dupont jumper wires set                                     | [Link to Jumper Wires](https://www.amazon.co.uk/40pcs-Dupont-Female-Jumper-Connectors/dp/B013EW65H2/ref=sr_1_28)                         | To connect load cell and HX711 to XIAO   |


