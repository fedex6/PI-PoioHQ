#	
#	Telegram: @fedex6
#
#---------------------#

import sys
import time
import datetime
import random
import telepot
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin names
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(18, GPIO.IN) #PIR1

bot = telepot.Bot('--TOKEN--')
print('\nIniciando PIRs ...\n' + time.ctime())

while 1:
    try:
		if GPIO.input(18):
			bot.sendMessage('chat_id from owner',"Se detecto movimiento en (1) " + time.ctime())
			time.sleep(2.9)
		time.sleep(0.1)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()