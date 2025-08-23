# smart-poop-bucket

Physical build:

![IMG_7241](https://github.com/user-attachments/assets/ec8b2981-2d34-4768-ab0d-ff2e8b9a50e1)

Smart 3D printer poop bucket suitable for the Bambu A1. Track your poop with the web interface. Uses a Xiao ESP32-S3, HX711 and a 50kg load cell. This very handy tool makes it easier to manage your (printer) poop, by allowing you to monitor live your poop grammage for each print. As I'm sure you know, the slicer's estimate is only just that - an estimate - and so when it is important to know the total filament usage, for example when calculating the cost of a 3D print to sell, this handy tool allows you to see the exact weight of poop output by the printer per print. Uses the public HX711 micropython lib, so this project is therefore shared under an MIT license.

Why did I create this? Well, simply put, I hate the waste produced by multicolour prints. I like to minimise my waste when printing, and also when I sell my multicolour prints I need to calculate the price by including the weight of the poop and the printed objects. So, I thought it would be really handy, rather than me having to empty my poop bin and weigh it myself every time, instead have a smart poop bin where I can keep track of the poop weight of each print, without having to go through the hassle of weighing it myself. This should make selling 3D prints easier for anyone who uses the AMS lite system with their A1.

**The poop bucket itself, with the minecraft chest theme:**

<img width="514" height="491" alt="image" src="https://github.com/user-attachments/assets/795cf7e5-d2ee-4e54-9dd7-ef567abc05d5" />

<img width="398" height="421" alt="image" src="https://github.com/user-attachments/assets/47c6a7d5-317f-4c00-b22a-73f305eb8440" />

**The PCB:**

<img width="432" height="217" alt="image" src="https://github.com/user-attachments/assets/ff7ab3db-a163-45bd-bd49-c3ccc98c8d29" />

**The base which houses the electronics and weigh scales - the chest goes on top of this**

<img width="556" height="254" alt="image" src="https://github.com/user-attachments/assets/e494c5bc-4fcf-4ee6-b7b1-925b1df8134d" />

**Bottom side of the base:**

<img width="343" height="344" alt="image" src="https://github.com/user-attachments/assets/78a72509-0299-4e2b-9557-bb75767f3fcf" />

**The chest and the base together:**

<img width="262" height="331" alt="image" src="https://github.com/user-attachments/assets/cd023d5d-0372-4005-b1b3-f0bdab65734b" />


```

Wiring diagram:

             ┌──────────────────────────────────────────────┐
             │                 Generic ESP32-S3             │
             │                                              │
             │ GPIO16 ────────► DT (HX711)                  │
             │ GPIO17 ────────► SCK (HX711)                 │
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
             │ A-    ◄─────── White wire (Load Cell)        │
             └──────────────────────────────────────────────┘


             ┌──────────────────────────────────────────────┐
             │                50kg Load Cell                │
             │                                              │
             │ Red   ───────► E+ (HX711)                    │
             │ Black ───────► E- (HX711)                    │
             │ White ───────► A- (HX711)                    │
             └──────────────────────────────────────────────┘

```


BOM:

| Quantity | Component                    | Model / Description                                      | Purchase Link                                                                                                                        | Cost (GBP) |
|----------|------------------------------|----------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|------------|
| 1        | Xiao ESP32-S3                | Xiao ESP32-S3 devboard                                   | [Link to ESP32-S3](https://www.aliexpress.com/item/1005007426784408.html?spm=a2g0o.productlist.main.1.28895274bF7p0T)                  | £9.19      |
| 1        | HX711 Load Cell Amplifier + 50KG | HX711 24-bit ADC module bundled with 50kg load cells | [Link to HX711 Load Cell](https://www.amazon.co.uk/Weighting-Half-bridge-Amplifier-Bathroom-Arduino/dp/B07FMN1DBN/ref=sr_1_45)         | £7.98      |
| 40       | Jumper Wires (male–female)   | Dupont jumper wires set                                  | [Link to Jumper Wires](https://www.amazon.co.uk/40pcs-Dupont-Female-Jumper-Connectors/dp/B013EW65H2/ref=sr_1_28)                       | £3.99      |
| 1        | Custom PCB                   | JLCPCB fabricated PCB                                    | [JLCPCB](https://jlcpcb.com)                                                                                                            | £1.57 ($2)     |
|          |                              |                                                          |                                                                                                                                        | **£22.73** |
