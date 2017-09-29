# Home Automation-Assembly 
CLICK [SLIDES ](https://docs.google.com/presentation/d/1zo2Fed9B6CcyHv5adE_SMtf5pZjYK_uYpe7jlIysYbU/edit#slide=id.g26c7365d2f_5_5)TO ACCESS THE WORKSHOP MATERIAL INCLUDING THE CIRCUIT DIAGRAM AND DETAILED STEPS TO RUN THE CODE 

This is a DIY workshop. Code for sending values from LDR to the website is given and based on that you need to program for rest of the sensors. For the network part, code is included in the network.py file and you to use it in the communication.py file to send data. 

STEPS: 

1. Download the folder
2. Upload the arduino_code_ldr.ino to Arduino IDE
3. Edit the communication.py file (publish key, subscribe key from pubnub and the port number for Arduino)
4. Write codes for arduino_code_ldr.ino, communication.py, automation.html files to display values appropriately
5. Edit the automation.html file (publish key and subscribe key from pubnub) 
6. Run the communication.py file first
7. Host the site online or open it in your browser and run it locally 

Visit ... to access the webiste which displays values from sensors and ... to access the website to control the lights.
