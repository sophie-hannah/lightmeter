# SPDX-FileCopyrightText: 2017 Tony DiCola for Adafruit Industries
# SPDX-FileCopyrightText: 2017 James DeVito for Adafruit Industries
# SPDX-License-Identifier: MIT

# This example is for use on (Linux) computers that are using CPython with
# Adafruit Blinka to support CircuitPython libraries. CircuitPython does
# not support PIL/pillow (python imaging library)!

import time, math
import subprocess

from board import SCL, SDA
import busio
from PIL import Image, ImageDraw, ImageFont
import adafruit_tsl2591


# Create the I2C interface.
i2c = busio.I2C(SCL, SDA)
#global isSen
isSen = False
isEyeLink=False
try:
    sensor = adafruit_tsl2591.TSL2591(i2c)
    isSen = True
    print("connected to LUX")

except:
    print("fuck")
# Create the SSD1306 OLED class.
# The first two parameters are the pixel width and pixel height.  Change these
# to the right size for your display!


from pylink import *
#from pygame import *
import time
import sys




class BroadcastEyelink(EyeLinkListener):
	def __init__(self):
		EyeLinkListener.__init__(self)
	



def previewTrackerConnection(tracker):
	print("preview trc")
	idata = tracker.getTrackerInfo()
	print(idata)# access link status info
	tracker.requestTime()         # force tracker to send status and time  - not implemented in pylink
	t = currentTime()
	print(t)
	while(currentTime()-t < 500):   # wait for response
		tt = tracker.readTime()   # will be nonzero if reply
		if(tt != 0):		# extract connection state
			if(idata._link_flags & LINK_BROADCAST):
				return LINK_BROADCAST;
			if(idata._link_flags & LINK_CONNECTED):
				return LINK_CONNECTED;
			else:
				return 0;
		tracker.pumpMessages();             # keep Windows happy
		if(tracker.breakPressed()):
			return 1;  # stop if program terminated
	return -1  # failed (timed out)


can_read_pixel_coords = False

def waitForConnection(tracker):
	print("waiting for connection ")
	first_pass = 1   # draw display only after first failure

	while(1):	# loop till a connection happens
			# check if tracker is connected
		i = previewTrackerConnection(tracker)
		if(i == -1):
			print("no tracker")
			alert("Cannot find tracker")
			
			#return -1
		elif(i > 0):
			print(" we have a connection")
			
			return 0  # we have a connection!

		if(first_pass):
			first_pass = 0#If not, draw title screen
			pass

		i = tracker.getkey()      #check for exit
		if(i==ESC_KEY or i==TERMINATE_KEY):
			return 1

		msecDelay(500);   #go to background, don't flood the tracker

def track_mode_loop(tracker,theSens):
  #theLuxMessage = 'Light: {0}'.format(math.floor(theSens.lux))
  #print(theLuxMessage)
  oldmode = -1;  # to force initial mode setup
  print(tracker.isConnected())
  while(tracker.isConnected()):
      mode = tracker.getTrackerMode()
      print("mode is mod")
      key = tracker.getkey()

      if(key==27 or tracker.breakPressed() or not tracker.isConnected()):
      	return
      
      elif(key):                  	# echo to tracker
        tracker.sendKeybutton(key,0,KB_PRESS)

      #if(mode == oldmode):
      #	continue
      print(mode)
      if(mode == EL_RECORD_MODE):        # Record mode: show gaze cursor
            #record_mode_display(tracker)
            # send messages
            
            print("a fake rubber squid")
            #print(isSen)
            
            try:
                print("try lux")
                theLuxMessage = 'Light: {0}'.format(math.floor(theSens.lux))
                print(theLuxMessage)
                tracker.sendMessage(theLuxMessage)
               
            except:
                print("sending light didnt' work")
            else:
                print("try  to get the senserlux")
                try:
                    print("try  to get the senserlux")
                    sensor = adafruit_tsl2591.TSL2591(i2c)
                    isSen = True
                except:
                    pass
                
           # only try this every 100ms
            msecDelay(100)
                
            
      elif(mode ==  EL_IMAGE_MODE):     # IMAGE NOT AVAILABLE IN BROADCAST
            pass

      elif(mode ==  EL_SETUP_MENU_MODE):  # setup menu: just blank display
                                    # read gaze coords in case changed
      	    if(tracker.isConnected() and can_read_pixel_coords):
               read_tracker_pixel_coords()

     
      else:                    # any other mode: transparent key (black)
            pass
      oldmode = mode


   

tracker = BroadcastEyelink()


tracker.setName("broadcast")
#while 99:
#    try
#while 1:
#    theLuxMessage = 'Light: {0}'.format(math.floor(sensor.lux))
#   print(theLuxMessage)
waitForConnection(tracker)
connectSting  = 1

while 22:
    
    try:
        
        tracker.broadcastOpen()
        while 1:
            try:
                print("starting a loop")
                track_mode_loop(tracker,sensor) # this quits on it's ownexcept:
                msecDelay(100)
            #except:

            except:
                pass
        
    except:
        print("help")
        conSting = "|%" * connectSting
        print(conSting)
        
    
        

        msecDelay(500)
    
    

  