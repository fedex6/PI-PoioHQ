#
#	Telegram: @fedex6
#
#---------------------#

#base coder TelegramBot:- Salman Faris

import os
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

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']

    #if chat_id == chat_id from owner :
    if 1:
        if command =='/roll':
            bot.sendMessage(chat_id, random.randint(1, 6))

        if command == '/id':
            bot.sendMessage(chat_id, chat_id)

        if command == '/iniciar':
            os.system('python pys/pir.py &')
            bot.sendMessage(chat_id,'Iniciada la deteccion de los PIRs')
            
        if command == '/stop':
            os.system('pkill -9 -f pir.py &')
            bot.sendMessage(chat_id,'Detenida la deteccion de los PIRs')

    else:
        bot.sendMessage(chat_id,'Sal de aqui maldito bastardo !')
        print(chat_id + ' intento usar el bot.\n')

bot = telepot.Bot('--TOKEN--')
bot.message_loop(handle)
print('Iniciando...')

while 1:
    try:
        time.sleep(0.5)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
