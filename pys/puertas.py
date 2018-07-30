#   
#   PoioHQ : Puertas
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
name_owner  =   '-- name without @ of owner --'

## Others
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin names
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up GPIO output channel
GPIO.setup(23, GPIO.IN) #Ventana

bot = telepot.Bot(token)

while 1:
    try:
        if GPIO.input(23):
            bot.sendMessage(chat_owner,"La ventana esta abierta " + time.ctime())
            ## LOG
            log = open('..log.txt', "a")
            log.write('[ ' + time.ctime() + ' ] >>> La ventana esta abierta\n')
            log.close()

        time.sleep(1)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()