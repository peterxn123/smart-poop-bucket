**Smart Poop Bucket**

Total time spent: 12h

*July 29th - Made a start*

For my highway project, I wanted to solve a real problem in my life. So I thought about it properly. I spent a while going around my house looking and thinking about things that I could solve with a hardware project. Then it hit me. What if I could help solve the bane of my existence as someone who 3D prints a lot - the piles of poop which I have to weigh every time I finish a print, if I want to sell it?
I thought if I could create a smart bucket with built in scales which weigh the poop for me, with an easily accessible interface to see the weight, then this would be very helpful!

So, I then spent a while deciding on the hardware.

I decided I wanted a web interface for my poop bucket to make the figures easy to access. For this reason I needed a dev board which was reasonably powerful with a wifi antenna. This is how I decided on the ESP32-S3, as it is a powerful yet cheap devboard which I have heard good things about in the past.
Then, for weighing the poop, I knew I needed a load cell, as I remembered researching them when I had to replace one on the auto calibrating bed of my 3D printer. So, I researched the most common and easiest way to implement a load cell which was also ocmpact enough to fit into a poop bucket. This is how I stumbled across the bundles of the very popular Hx711, which was actually the top choice on google, and a few load cells aswell, in a conveient yet affordable bundle.

So there it was, my parts were decided and I was ready to go. I was excited for what was to come next.

*Time spent: 3h*

<img width="1259" height="707" alt="image" src="https://github.com/user-attachments/assets/4ab2e882-c156-4e58-9408-ef54fdcccbc5" />


*July 30th - Worked on firmware*

I decided that today was the time to work on firmware. After thinking for a while, I decided that the best way to approach this was with micropython, as a library for the HX711 already existed. Also, micropython is something I am familiar with as I have used it a lot with Pi Picos in the past, so I thought it was best to go ahead with something I was familiar with. 

I knew I wanted a HTML site accessible on the local network, usable to monitor the status of the poop bucket and how much weight was in it. I decided to enlist the help of Github Copilot, and used it to help me verify the code I wrote. 
I began by researching how to use the HX711 library, imported it, and wrote some basic code for initialising it. I then added the HTML functionality, creating a simple HTML site and then hosting it. Github CoPilot helped me with the calibration part of the scales as I couldn't figure that out, and it also helped me link up the html to the PY as this was not something I had done before.

In the end, after much tinkering and consultation with both AI and a friend I created something that looked decent, and that my friend said would likely work, so I was happy with it.

<img width="912" height="792" alt="image" src="https://github.com/user-attachments/assets/1bd8fbd7-5f41-4507-968e-35d2d4a0e002" />

*Time spent: 4h*

*July 31st - CAD and polish*

Finished my project today. I knew I had to get a quick start on the CAD as the highway deadline was coming up. I knew the best way to approach this would be to find a reference poop bucket design to use for my dimensions and to ensure that my own poop bucket is accurately sized. I found a design by Encrust3D on Makerworld called 'Slim A1 poop bucket'. I knew this was perfect as it had loads of positive reviews as fitting perfectly for the A1, and this is exactly what I wanted to use this poop bucket with my Bambu A1. 

So I imported the file into Fusion 360 and took some measurements. The length was 180mm, width 80mm and height 110mm. There was a cutout in the corner of 50x40mm, to make the bucket fit around the printer. 

I jumped into Fusion again, creating another file and started my sketch. I used similar dimensions, so that my bucked would fit just as well. I then extruded upwards, 20mm, then hollowed it out, by 16mm, leaving a 5mm gap on the edges. I then added the walls upwards to 110mm, to catch any flying poop and then added fillets, to make the look of the bucket better.
I decided to add a bit of flair to my design by adding a poop inset and the words 'Le poop' on the side.

This was just the bucket, however. I still needed to create the electronics enclosure housing the strain gauge that this bucket would sit on. I decide to make it the same dimensions as the bucket, to give it a seamless look. 

I then had to think about how to ensure that the strain guage could properly capture the buckets weight. I decided to add some holes inset into the base and matching dimples on the bucket which would slot in, to ensure the bucket stayed in place in one place, so the strain guage could stay well calibrated.

I then imported 3D models for all my electronics, placing in the HX711 and ESP32. I positioned them both and then created the cutout for the USB C ports.

Then, I extruded upwards and placed the imported strain guage down. I ensured that there was a gap under the part of the strain guage that measures weight, to ensure proper functionality. I adjusted the height of the strain guage until it was just sticking out of the case so it could touch the bucket.

I was now happy overall with the design, and I brought the two models together in Fusion and they matched perfectly. 

Today was a great learning experience in Fusion and it was a good opportunity to practice my CAD skills.

<img width="970" height="656" alt="img" src="https://github.com/user-attachments/assets/a14dd543-3f94-4b3a-8704-4e0a269f45f3" />

*Time spent: 5h*


*August 5th - building back from rejection*

My project got rejected today. Originally it was wihtout an option to resubmit, but I asked if I could anyway as I knew I had to have a project finished for my stipend. I don't mind the rejection though, as it is an opportunity to learn and improve on what I've built. So today I started by first deciding on what would improve my project. My reviewer, Kai, suggested if it was themed around something then it would stand out, and have a higher chance of being approved. He suggested a minecraft chest as an example, and after thinking about it for a bit I decided that this was a perfect theme, especially when I could print it multicolour with my AMS. 
So today the first thing that I improved, polished and gave it Minecraft theming is the firmware. The most important part to be polished is the part the user sees, no? This file, which would be hosted by the ESP - index.html - was previously incredibly bland and I'm sure this was a factor in my rejection. So, while keeping the same fundamental features, I completely redid the styling on the site by moving sections around and completely redoing the CSS. I also added clear indicators of when things weren't loading right and a refresh button if needed. The underlying scripts which connected with the ESP remained the same, while the interface the user uses was completely revamped and properly fit in to the Minecraft chest theme. I spent plenty of time on this, which I was happy to do as the end result was something very clean and polished, in my opinion.

<img width="958" height="849" alt="image" src="https://github.com/user-attachments/assets/75756ddc-d1c5-43b9-9805-24fc45037592" />

*Time spent: 3 hours*


*August 6th - CAD and PCB grind*

I started today by reviewing my CAD. I jumped into Fusion, moved the window to one half of my screen then put a reference image of a minecraft chest on the other half. I started first by creating a sketch of a square of the same width as my old bucket, but with the depth now the same as the width to create the cube structure minecraft blocks have. I then extruded upwards, creating the bottom half of my open chest with the minecraft design already coming together.
Then I created the top half, sticking with the same width and height but a smaller depth obviously (it was vertical). At this point, the top half was just floating in mid-air behind the bottom half - obviously this would not be printable.
I only realised my mistake when Kai told me to double check everything is printable - obviously it wasn't. I fixed this by connecting them with a sketch of an arc which I then extruded creating a curve that connected the halves. 
But this design was only the bucket so far. I then designed the base which housed the electronics. I wanted it to be nearly invisible so the minecraft chest bin could take center stage - so I made its dimensions 15mm smaller than the chest's so it could hide underneath. I extruded it upwards 25mm, rounded out the corners to polish the design, and imported all the electronics parts CAD models. I used these models to create a cutout for the USB-C port on the ESP and to ensure the platform I extruded for the load cell to sit on had the right dimensions. I exported these CAD files, and added them to the repo. I was happy with my work. 

<img width="166" height="220" alt="image" src="https://github.com/user-attachments/assets/0a98a5da-cf63-476a-bed5-d38a900270ff" />

After talking to my reviewer, Kai, again, he said that the only way he could give me 4 points for my highway project, which is what I need to get my travel stipend, is if I created a PCB for it. So this is exactly what I did. I decided that the best way to go about this would be to have the MCU SMD mounted onto the PCB, then it would have traces running off it to the sides of the PCB where there would be labelled pads which i would solder wires to, to connect the separate HX711 board and load cell to the PCB.
I first created the schematic, trying to keep it as clean as possible by separating each electronic componenet and using global labels to show their connections. I used 'testpoints' for the HX711 and load cell connections so I could have one for each connection needed to these, and then each of these could be assigned the footprint of a pad which could be easily placed on the PCB.
I then moved from the schematic editor to the PCB editor, where I first placed down the MCU then arranged the pads so tracing between them would be and look as clean as possible. I then routed my traces, keeping them neat and organised, to keep up an overall very polished appearance of the PCB. It was really helpful to have KiCAD showing me, before I routed, which components connected together as this made it easy to arrange the pads properly for the best tracing. I added an outline of the board, using arcs for round corners and lines to join them together. I then added some silkscreen, outlining where the pads for each component are on the front and then a secret message on the back. Overall this PCB design process was very enjoyable and I was very happy with the finished product.

<img width="864" height="433" alt="image" src="https://github.com/user-attachments/assets/72e90c62-2d2d-4035-a67b-12f99e3fab49" />

*Time spent: 6 hours*
