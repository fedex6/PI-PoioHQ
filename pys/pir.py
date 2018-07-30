#	
#	PoioHQ : PIRs
#---------------------#

## Basic imports
import os
import sys
import time
import datetime
import telepot

## Bot data
token       =   '-- TOKEN --'
chat_owner  =   '-- # of chat owner --'
name_owner  =   '-- name without @ of owner --'

## Others
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin names
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up GPIO output channel
GPIO.setup(18, GPIO.IN) #PIR1
GPIO.setup(5, GPIO.IN) #PIR2

bot = telepot.Bot(token)

while 1:
    try:
        if GPIO.input(18):
            bot.sendMessage(chat_owner,"Se detecto movimiento en el cuarto " + time.ctime())
            ## LOG
            log = open('..log.txt', "a")
            log.write('[ ' + time.ctime() + ' ] >>> Movimiento detectado en el cuarto\n')
            log.close()
            time.sleep(2.9)
        
        if GPIO.input(5):
            bot.sendMessage(chat_owner, "Se detecto movimiento en el comedor " + time.ctime())
            ## LOG
            log = open('..log.txt', "a")
            log.write('[ ' + time.ctime() + ' ] >>> Movimiento detectado en el comedor\n')
            log.close()

        time.sleep(1)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()