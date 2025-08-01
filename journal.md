**Smart Poop Bucket**

*July 29th - Made a start*

For my highway project, I wanted to solve a real problem in my life. So I thought about it properly. I spent a while going around my house looking and thinking about things that I could solve with a hardware project. Then it hit me. What if I could help solve the bane of my existence as someone who 3D prints a lot - the piles of poop which I have to weigh every time I finish a print, if I want to sell it?
I thought if I could create a smart bucket with built in scales which weigh the poop for me, with an easily accessible interface to see the weight, then this would be very helpful!

So, I then spent a while deciding on the hardware.

I decided I wanted a web interface for my poop bucket to make the figures easy to access. For this reason I needed a dev board which was reasonably powerful with a wifi antenna. This is how I decided on the ESP32-S3, as it is a powerful yet cheap devboard which I have heard good things about in the past.
Then, for weighing the poop, I knew I needed a load cell, as I remembered researching them when I had to replace one on the auto calibrating bed of my 3D printer. So, I researched the most common and easiest way to implement a load cell which was also ocmpact enough to fit into a poop bucket. This is how I stumbled across the bundles of the very popular Hx711, which was actually the top choice on google, and a few load cells aswell, in a conveient yet affordable bundle.

So there it was, my parts were decided and I was ready to go. I was excited for what was to come next.

<img width="1259" height="707" alt="image" src="https://github.com/user-attachments/assets/4ab2e882-c156-4e58-9408-ef54fdcccbc5" />


*July 30th - Worked on firmware*

I decided that today was the time to work on firmware. After thinking for a while, I decided that the best way to approach this was with micropython, as a library for the HX711 already existed. Also, micropython is something I am familiar with as I have used it a lot with Pi Picos in the past, so I thought it was best to go ahead with something I was familiar with. 

I knew I wanted a HTML site accessible on the local network, usable to monitor the status of the poop bucket and how much weight was in it. I decided to enlist the help of Github Copilot, and used it to help me verify the code I wrote. 
I began by researching how to use the HX711 library, imported it, and wrote some basic code for initialising it. I then added the HTML functionality, creating a simple HTML site and then hosting it. Github CoPilot helped me with the calibration part of the scales as I couldn't figure that out, and it also helped me link up the html to the PY as this was not something I had done before.

In the end, after much tinkering and consultation with both AI and a friend I created something that looked decent, and that my friend said would likely work, so I was happy with it.

<img width="912" height="792" alt="image" src="https://github.com/user-attachments/assets/1bd8fbd7-5f41-4507-968e-35d2d4a0e002" />

*Time spent: 4h*
