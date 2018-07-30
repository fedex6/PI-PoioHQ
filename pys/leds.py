#   
#   PoioHQ : Leds
#---------------------#

## Basic imports
import os
import sys
import time
import datetime

## Others
import RPi.GPIO as GPIO

# to use Raspberry Pi board pin names
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# set up GPIOs
GPIO.setup(18, GPIO.IN) #PIR1
GPIO.setup(4, GPIO.OUT) #LED PIR1
GPIO.setup(5, GPIO.IN) #PIR2
GPIO.setup(22, GPIO.OUT) #LED PIR2

GPIO.setup(23, GPIO.IN) #Ventana
GPIO.setup(17, GPIO.OUT) #LED Ventana
#GPIO.setup(6, GPIO.IN) #Puerta
#GPIO.setup(27, GPIO.OUT) #LED Puerta

## APAGAR LOS LEDS
GPIO.output(4, False)
GPIO.output(22, False)
GPIO.output(17, False)
#GPIO.output(27, False)

while 1:
    try:
        ## PIRs
        if GPIO.input(18): ## Se detecto movimiento
            #print('movimiento cuarto')
            GPIO.output(4, True)
            time.sleep(1)
        else:
            GPIO.output(4, False)
        
        if GPIO.input(5):
            #print('Movimiento Comedor')
            GPIO.output(17, True)
            time.sleep(1)
        else:
            GPIO.output(17, False)

        ## Ventana
        if GPIO.input(23): ## Esta la ventana abierta
            #print('Ventana Abierta')
            GPIO.output(22, True)
        else:
            GPIO.output(22, False)
        time.sleep(0.2)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        ## Apagar los Leds
        GPIO.cleanup()
        exit()