# smart-poop-bucket
Smart 3D printer poop bucket suitable for the Bambu A1. Track your poop with the web interface. Uses an ESP32-S3, HX711 and a 50kg load cell. This very handy tool makes it easier to manage your (printer) poop, by allowing you to monitor live your poop grammage for each print. As I'm sure you know, the slicer's estimate is only just that - an estimate - and so when it is important to know the total filament usage, for example when calculating the cost of a 3D print to sell, this handy tool allows you to see the exact weight of poop output by the printer per print. Uses the public HX711 micropython lib, so this project is therefore shared under an MIT license.

Why did I create this? Well, simply put, I hate the waste produced by multicolour prints. I like to minimise my waste when printing, and also when I sell my multicolour prints I need to calculate the price by including the weight of the poop and the printed objects. So, I thought it would be really handy, rather than me having to empty my poop bin and weigh it myself every time, instead have a smart poop bin where I can keep track of the poop weight of each print, without having to go through the hassle of weighing it myself.

<img width="514" height="491" alt="image" src="https://github.com/user-attachments/assets/795cf7e5-d2ee-4e54-9dd7-ef567abc05d5" />

<img width="398" height="421" alt="image" src="https://github.com/user-attachments/assets/47c6a7d5-317f-4c00-b22a-73f305eb8440" />

<img width="432" height="217" alt="image" src="https://github.com/user-attachments/assets/ff7ab3db-a163-45bd-bd49-c3ccc98c8d29" />

<img width="556" height="254" alt="image" src="https://github.com/user-attachments/assets/e494c5bc-4fcf-4ee6-b7b1-925b1df8134d" />


```

Wiring diagram:

             ┌──────────────────────────────────────────────┐
             │                 Xiao ESP32-S3                │
             │                                              │
             │ GPIO2 ────────► DT (HX711)                   │
             │ GPIO3 ────────► SCK (HX711)                  │
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

| Quantity | Component                            | Model / Description                                         | Purchase Link                                                                                                                        | Notes                                     |
|----------|--------------------------------------|-------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------|
| 1        | Xiao ESP32-S3                             | Xiao ESP32-S3 devboard.                                  | [Link to ESP32-S3](https://www.aliexpress.com/item/1005007426784408.html?spm=a2g0o.productlist.main.1.28895274bF7p0T&algo_pvid=9b4b8494-2fd5-45ef-af4a-c2368d63462d&algo_exp_id=9b4b8494-2fd5-45ef-af4a-c2368d63462d-0&pdp_ext_f=%7B%22order%22%3A%2283%22%2C%22eval%22%3A%221%22%7D&pdp_npi=6%40dis%21GBP%2110.79%2110.79%21%21%2113.93%2113.93%21%40210385db17544911680423756e8d46%2112000040715643563%21sea%21UK%213302944909%21X%211%210%21&curPageLogUid=e3blD8fJ3AUt&utparam-url=scene%3Asearch%7Cquery_from%3A)        | Main MCU with Wi-Fi + USB-C               |
| 1        | HX711 Load Cell Amplifier + 50KG     | HX711 24-bit ADC module bundled with 50kg load cells.       | [Link to HX711 Load Cell](https://www.amazon.co.uk/Weighting-Half-bridge-Amplifier-Bathroom-Arduino/dp/B07FMN1DBN/ref=sr_1_45)           | Amplifies load cell signal               |
| 40       | Jumper Wires (male–female)           | Dupont jumper wires set                                     | [Link to Jumper Wires](https://www.amazon.co.uk/40pcs-Dupont-Female-Jumper-Connectors/dp/B013EW65H2/ref=sr_1_28)                         | To connect load cell and HX711 to XIAO   |


