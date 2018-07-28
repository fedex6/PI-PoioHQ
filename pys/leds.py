#	
#	PoioHQ : LEDs Indicadores
#---------------------#

## Basic imports
import os
import sys
import time
import datetime
import telepot

## Others
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin names
GPIO.setmode(GPIO.BCM)

# set up GPIOs
GPIO.setup(18, GPIO.IN) #PIR1
GPIO.setup(4, GPIO.OUT) #LED PIR1

GPIO.setup(22, GPIO.OUT) #LED PIR2


GPIO.setup(17, GPIO.OUT) #LED PUERTA1


GPIO.setup(27, GPIO.OUT) #LED PUERTA2

## APAGAR LOS LEDS
GPIO.output(4, False)

while 1:
    try:
        if GPIO.input(18): ## Si detecta movimiento, prende el led
            GPIO.output(4, True)
            GPIO.output(22, True)
            GPIO.output(17, True)
            GPIO.output(27, True)
            time.sleep(1)
        else:
            GPIO.output(4, False)
            GPIO.output(22, False)
            GPIO.output(17, False)
            GPIO.output(27, False)
            time.sleep(2)
        time.sleep(0.1)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
