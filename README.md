# smart-poop-bucket
Smart 3D printer poop bucket suitable for the Bambu A1. Track your poop with the web interface.

Why did I create this? Well, simply put, I hate the waste produced by multicolour prints. I like to minimise my waste when printing, and also when I sell my multicolour prints I need to calculate the price by including the weight of the poop and the printed objects. So, I thought it would be really handy, rather than me having to empty my poop bin and weigh it myself every time, instead have a smart poop bin where I can keep track of the poop weight of each print, without having to go through the hassle of weighing it myself.


```

Wiring diagram:

┌───────────────────────────────────────────────────────────────┐
│                         XIAO ESP32-C3                         │
│                                                               │
│      D4 (GPIO4) ────────────────► HX711 DT (DOUT)             │
│      D5 (GPIO5) ────────────────► HX711 SCK (PD_SCK)          │
│         3V3     ────────────────► HX711 VCC                   │
│         GND     ────────────────► HX711 GND                   │
│                                                               │
│       USB-C: power and programming                            │
└───────────────────────────────────────────────────────────────┘

                      │
                      ▼

┌───────────────────────────────────────────────────────────────┐
│                        HX711 Amplifier                        │
│                                                               │
│     DT (DOUT)  ◄─────────────── XIAO GPIO4 (D4)               │
│     SCK        ◄─────────────── XIAO GPIO5 (D5)               │
│     VCC        ◄─────────────── XIAO 3V3                      │
│     GND        ◄─────────────── XIAO GND                      │
│                                                               │
│     E+ (Red)   ◄─────────────── Load Cell (Excitation +)      │
│     E- (Black) ◄─────────────── Load Cell (Excitation –)      │
│     A+ (Green) ◄─────────────── Load Cell (Signal +)          │
│     A- (White) ◄─────────────── Load Cell (Signal –)          │
└───────────────────────────────────────────────────────────────┘

                      │
                      ▼

┌───────────────────────────────────────────────────────────────┐
│                         50kg Load Cell                        │
│                                                               │
│     Red    ───────────────► HX711 E+                          │
│     Black  ───────────────► HX711 E–                          │
│     Green  ───────────────► HX711 A+                          │
│     White  ───────────────► HX711 A–                          │
└───────────────────────────────────────────────────────────────┘


```
