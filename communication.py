import sys

import os
from time import sleep
from pubnub.callbacks import SubscribeCallback
from pubnub.pubnub import PubNub, SubscribeListener
from pubnub.enums import PNStatusCategory
from pubnub.pnconfiguration import PNConfiguration
from pubnub.pubnub import PubNub
from pubnub.enums import PNOperationType, PNStatusCategory 
import serial 


ser = serial.Serial('/dev/cu.usbmodem1421', 9600) #change this line to ser = serial.Serial('COM8', 9600) if you are using windows. Change the port number/ COM according to arduino ide

pnconfig = PNConfiguration() 
pnconfig.subscribe_key = 'sub-c-f59674be-a2c8-11e7-90db-92dc6f0eccb3'
pnconfig.publish_key = 'pub-c-9aa1dba9-30d0-4e1b-9a20-dd440f54c3d7' 
pubnub = PubNub(pnconfig)
channel = 'auto_value'  


pnconfig1 = PNConfiguration()
pubnub1 = PubNub(pnconfig)

#Publishes data to pubnub and also subscribe to the channel auto_control
class MySubscribeCallback1(SubscribeCallback):
    def status(self, pubnub1, status):
        pass
    
    def presence(self, pubnub1, presence):
        pass  # handle incoming presence data
 
    def message(self, pubnub1, message):
        print('will now write something') 
        print(message.message) 

        if (message.message == 'a'):  
        	ser.write('a') 
        elif (message.message == 'b'): 
        	ser.write('b')
        print(message.message) 
        


pubnub1.add_listener(MySubscribeCallback1())
pubnub1.subscribe().channels('auto_control').execute()



#Subscribe to the channel auto_value
class MySubscribeCallback(SubscribeCallback):
    def status(self, pubnub, status):
        pass
    
    def presence(self, pubnub, presence):
        pass  # handle incoming presence data
 
    def message(self, pubnub, message):
        print(message.message)
        
      

pubnub.add_listener(MySubscribeCallback())
pubnub.subscribe().channels(channel).execute() 

#read data from arduino serial and publish it to pubnub
def reading(): 
	while(True):
		try:
			print('reading...')
			sleep(2)
			data = ser.readline()	#read from the serial and save in a variable
			print(data)
			data = data.rstrip()	#remove the \n from the string
			if(data =='1' or data=='0'):	#change accordingly, how you add all the sensor data
				pubnub.publish().channel(channel).message(data).sync()
		except KeyboardInterrupt:
			ser.close()


if __name__ == '__main__': 
	reading()
