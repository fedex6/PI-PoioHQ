#	
#	Telegram: @fedex6
#
#---------------------#

import sys
import time
import datetime
import telepot
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin names
GPIO.setmode(GPIO.BCM)

# set up GPIO output channel
GPIO.setup(18, GPIO.IN) #PIR1

bot = telepot.Bot('--TOKEN--')

while 1:
    try:
        if GPIO.input(18):
        bot.sendMessage('chat_id from owner',"Se detecto movimiento en (1) " + time.ctime())
        ## LOG
        log = open("../log.txt", "a")
        log.write('[ ' + time.ctime() + ' ] >>> Movimiento detectado en (1)\n')
        log.close()
        time.sleep(2.9)
        time.sleep(0.1)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()