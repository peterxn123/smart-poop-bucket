**Smart Poop Bucket**

**Designing**

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

**Physical Build**

*August 9th - Got the grant and ordered the parts so I can build it on holiday*

Today, quite a few days after Kai approved my revised project, I received an email from Jonathan letting me know I would be receiving a grant in my email in a short while and - lo and behold - a couple minutes later I got an email from HCB giving me the details of my grant! But there was a problem... Tomorrow I am going on holiday to Turkey and the time that I received the grant meant that I wouldnt be able to order parts to my house and get them in time... So the only way to get my parts before the deadline is to order them to the resort and put my trust in the courier survices of Turkey. I've ordered them off Amazon - let's just wait and hope.

<img width="500" height="229" alt="image" src="https://github.com/user-attachments/assets/6c022bd9-2485-458b-b44e-a28deb5bb013" />

*August 14th - It's the deadline... and I still haven't got my parts...*

Uh oh! Yeah, no parts. Seems like the courier service the seller used here in Turkey, named 'kolay gelsin' which translates, according to google at least, to 'good luck' is actually not as lucky as their name would say they are. I ordered my parts on the 9th, and they were meant to arrive on the 12th, but they still haven't arrived. I have contacted Amazon and they said they will investigate and they can see there is a delay with the courier company, but as I am writing this it is 10pm on the 14th so I have an inkling I won't get my parts in time for the deadline today. This was super dissapointing, but I have asked Acon from Hack Club if I could get an extension and they, being the kindest person ever, have said I can have an extension until early next week. I should be home by then so I can get the parts delivered using UK amazon which I know I can rely on. For now, I've re-ordered the parts and they should be there when I get home.

![IMG_7445](https://github.com/user-attachments/assets/22cb1844-4b5d-444f-a7f5-e639343cf0e8)


*August 19th - I'm home and hacking away*

Got back from my holiday today, and opened the front door at about 2am today to see two amazon parcels on the floor which had been posted through the letter box. These are the parts! First thing I did was sleep, because well, that's important and travelling's exhausting. Then I cracked open the parts and took a look at the loot. 4x Load Cells, 1x HX711 sensor, a pack of 40 jumper wires which I'll use to connect the components, and an ESP32-S3 board. 

After cracking open the parts, I started by taking a look at the wiring diagram of the ESP32 which was on a QR code included in the box. I did this because I knew it would help if i got all the needed wires soldered to where they need to be on the ESP, then attached the components to these wires so there'd be no mixing up where they need to connect to the microcontroller. From earlier work researching the HX711, I know I need 2 standard GPIO pins to connect to DT and SCK, and the 3V3 and GND connections. From looking at the HX711 lib docs, admittedly with some help from AI, I know that the data lines can be handled by any free, non hardware reserved GPIO pin.

So I soldered wires to GPIO16 and GPIO17 for DT and SCK, then 3V3 and GND. I made sure to use different coloured wires for each connection so I wouldn't mix them up later. I used purple for VCC, black for GND, white for DT and grey for SCK.

I'm pretty new to soldering, so I'm embarassed to say that this took me quite a while, and before I knew it the day was up. 

![IMG_7155](https://github.com/user-attachments/assets/0816de06-04ef-49d4-b1db-5768bda1257f)
![IMG_7156](https://github.com/user-attachments/assets/99d68114-4033-44ac-8001-b8ed0df023d7)


*Time spent: 2 and a half hours*


*August 20th - More soldering with the HX711*

Today I continued wiring the bits together. I started by taking out one load cell and the HX711 out of their packaging. I needed to solder the load cell to the HX711 so the HX711 can translate the input from the load into something the ESP can understand. This is obviously because the load cell is analogue, so you can't just wire it directly to the ESP. The load cell has 3 wires - black, white and red. I wasn't entirely sure which wire went to which pad on the HX711, especially considering there is 3 wires and 6 pads. So I asked ChatGPT to look at the docs of the HX711 and the load cell which I purchased and tell me. It told me that the black cable goes to E-, red to E+, and white to A-. So I spent some time soldering this in, which was admittedly annoying and I burned myself because the load cell wires are very thin and heated up a lot, but I managed to get a strong connection in the end. 

![IMG_7154](https://github.com/user-attachments/assets/646ecda3-965f-450f-b86d-dce6587cf47f)

*Time spent: 2 hours*


*August 21st - Finishing the soldering and moving onto the software...*

Today I started with finishing my soldering. This entailed the should be easy, but still took me more than an hour task of soldering the other ends of the  5 wires I previously soldered to the ESP, to the pads on the right side of the HX711. These pads are labelled GND, DT, SCK and VCC. GND and VCC are obvious - I soldered GND to the black wire I connected to the GND pin of my ESP, and soldered the VCC pad to the purple wire I previously connected to the 3V3 pad of my ESP. For the other 2 - DT and SCK - these are the data lines which send out the data from the load cell. These can be connected to any GPIO pin and so I just soldered DT to the white wire I had previously connected to GPIO 16 and SCK to the grey wire I had previously soldered to GPIO 17. By doing this, my soldering was finished.

So, it was time to do software after finishing the soldering. I purchased a very generic ESP32 from Amazon, so I had to figure out how to first connect it to my PC, then how to download micropython on it. To be honest, this was my first ever time using an ESP but I had heard great things about them so I was happy to dive right in. To program the ESP with micropython I followed the official guide online (https://micropython.org/download/ESP32_GENERIC_S3/), used esptool to flash it and this went smoothly! It showed up as a micropython device in my computer and I checked using Thonny just as a basic check to see if I could program some basic code on it and it worked! So I was happy that my PC was connected to the ESP and that it was programmed with Micropython, ready for uploading my firmware.

I started by uploading the python I had written before actually receiving the parts. I used thonny for this - partly because its very simple for interfacing with micropythond devices and also because I'm used to it from projects I used to do with my pico. Before uploading it, I just modified the DT and SCK pins listed in the code to 16 and 17, to match what was actually connected. I also added in my network SSID and password so the ESP could connect to my network. I uploaded the code to the ESP, then accessed the web interface... and it didn't work... Oh well, I expected this, considering I wrote the code without having the parts yet. I will try and take a look at this tomorrow.

One thing I did notice though, even without taring or anything, was that by just printing the raw data I was receiving from the HX711... there was no difference between the data I was getting when there was a weight on the load cells or not. So I figured there must be an issue. I googled it, and did a bit of consulting with chatGPT and checking of the amazon page where I bought my load cells from, and realised that with the 3 wire type of load cell that I have, to actually get a proper reading you need two of them wired to the HX711 so that it can compare their values and figure out the load placed on them. It's actually the more expensive 4 wire type of load cell that you only need one of. This is no problem though as I can fix it, and I'm especially glad I caught it early. I hopped into fusion very quickly and did a quick modification of my design so that rather than one raised platform in the middle for one load cell there is now two next to each other. Sent this print off to the printer, and it should be done by tomorrow. I also needed to solder the second load cell on. Looking at the HX711 documents I found online, to connect 2 3 wire load cells you have one of them connected as I already have connected, and then the second one goes on with red and black going to the same A+ and A- as the other load cell - they share these connections. Then for the white wire, the second one went to A+ as my first one was on A-. 

![IMG_7168](https://github.com/user-attachments/assets/32b6bf72-ba25-4d2d-be02-604d69b99817)

*Time spent: 4 hours*


*August 22nd - Putting the bits together, working on the software*

I woke up this morning to a nicely finished, clean print of the new base. I took it upstairs and test fitted the two laod cells and they fit perfectly. I also test fit the chest shape top, and it also fit perfetly with its pins alligning well and it touching the pads of the load cells perfectly. So, I decided that it was time to put the parts together and have it ready for some proper software work. I started by gluing the load cells into their respective positions on the base. I then placed the ESP and HX711 into the case aswell, moved the internal wires around a bit until they fit properly, plugged a usb c cable into the ESP and ran it through the channel I left in the base so I could easily plug it into my computer and then placed the chest bucket part on top. Overall, a clean looking build.

After plugging the ESP into my computer, I fired up Thonny and opened my main.py file to get some work done and get it functioning properly. First thing I knew I would need is a zero function - just to set the value of the scale to zero just how you tare a kitchen scale before you weigh anything on it. This was easy to implement using the 'set offset' function already available within the HX711 library I used. This was easy to find after persuing the docs for a short while. When the /tare function is called on the web server, it takes an average of 15 readings of the raw input from the HX711 then uses the 'set_offset' function to set the current reading as the offset, to offset it back to zero. Second fundamental thing I knew I would need to do to make my scale, and any scale for that matter, to get some proper weight reading in grams out of the analoge signal that the HX711 outputs, was to set up a calibration function. This essentially means placing a known weight onto the scale, like a bottle of water weighing 500g, then telling the computer what it weighs and it calculates the ratio between the input it has and grams, to figure out how many raw input units = 1 gram and then it uses this to display every reading after that with the correct weight in grams. I first added /calibrate as an endpoint, just like all the other endpoints I added before but also added an argument to it - so /calibrate?w=500 means you are saying the weight you have on the scale is 500g. It then does a reading of the raw value like before, by taking it 15 times and taking the average. It then figures out the difference between the current raw value and the currently set offset, to get the actual raw value of our calibration weight, in this case 500g. It then divides the difference by the known weight to get the ratio - this is raw units per gram. It then stores it in calib.json so it persists even after unpluging and replugging the ESP. It then sends a response so you can use it from the web interface and it knows the calibration has been stored successfully. I'm really proud of myself for creating these endpoints myself, with minimal help from AI.

Checking it myself in thonny, by sort of having it in a 'debug mode' of sorts by just printing the value of the raw value and gram value and the offset variables ever few seconds, I can see that the tare endpoint is correctly storing an offset, and after placing a 500g bottle of water on the scales in the chest and manually calling the calibration endpoint I can see this is working too. I then placed another known weight in the chest after calibrating and the gram value is actually surprisingly accurate, so I'm happy the calibration and taring are doing their jobs properly. Excited to finish this tomorrow.

![IMG_7231](https://github.com/user-attachments/assets/2fd31ff0-fb60-4ff4-9c5c-2cdb517ccb2c)

*Time spent: 5 hours*


*August 23rd - finishing it off and submitting*

Okay, sure it works right now if you manually call every endpoint and observe the readings yourself in the thonny console, but is this really how anyone wants to use it? Certainly not me. I need to get the web interface working. My problem right now is that I can't get it to ever show up when trying to get the micropyton to host it from its own internal memory. It keeps saying it doesn't exist, even though I have definitely uploaded the index.html file to the ESP's root multiple times though. Oh well though, this is only a minor hiccup, as if the endpoints work when manually calling them using the ESP's IP on my browser, and all thats happening when the web interface communicates with the ESP is its calling localhost, then surely I can just run the HTML on my PC locally, and just replace localhost with the ESP's IP? It was a really easy fix to make, and for ease of use I changed every reference to localhost to a single variable which can be changed if the IP of your ESP ever changes, or it's just really handy for first time use when configuring the web portal with the ESP's IP - instead of typing it multiple times you only have to type it once. So, after doing all this and changing the variable value to the IP of my ESP it... works! Yay! Well, almost. Previously I had only programmed in the start and stop functions into the web portal and sure, these do communicate with the endpoints properly and update the values appropriately in the table below, but they are also useless unless you can tare and calibrate the scale using the web portal aswell, because an untared and uncalibrated scale is not useful for weighing, well, anything. So I needed to add the tare and calibrate features to the web portal. First I started with the tare, because this was extremely easy. I just copied the 'stop' button over, changed its colour and then instead of making it call the '/stop' endpoint I made it call the '/tare' endpoint. Easy, right? Then, I moved onto the calibrate function which was a tougher nut to crack but still not very hard. Started by copying over the tare button, changing its colour again, changing the text within it to calibrate instead of tare. Then, I modified the JS function for the onclick of this button so that instead of immediately calling the endpoint it first makes this HTML element visible which is normally invisible then here you can type in the weight of the known weight you have put on the scales, THEN it sends this off to the ESP endpoint, and whatever weight you have put into the input box is put into the final API call, so it ends up being /calibrate?w=whateveryoutyped. And.. thats a wrap! The calibrate and tare functions work, which i tested by making the ESP print when it received an API call, and indeed it did after double checking in the console! Everything stores nicely on the table and you can see the delta of the weight of each print between pressing start and stop and even persists after a reboot! Really handy for printer poop measuring.

It works! Am I surprised?... Very! But yeah, it works and its pretty accurate wehn comparing the readings it picks up compared to my kitchen scales (i think anyway, because my kitchen scales only go down to 1g increments, rather than 0.1 of a gram). Last thing I did was takes some pictures, a demo video and submitted it to the highway demo form.

It's been a good ride, and a good build!

If you've made it to the end, thanks! You're a really cool person. :D

![IMG_7241](https://github.com/user-attachments/assets/71067e45-401f-4832-bae0-5cd523174a18)

*Time spent: 4 hours*


