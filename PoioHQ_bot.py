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
        if command =='/roll': ## Es solo de prueba, para ver si funciona el bot
            bot.sendMessage(chat_id, random.randint(1, 6))

        if command == '/id': ## Devuelve el numero de id del chat, para luego configurar para que solo lo use el dueño [probar otros metodos]
            bot.sendMessage(chat_id, chat_id)

        if command == '/iniciar': ## Inicia la deteccion de movimiento
            os.system('python pys/pir.py &')
            bot.sendMessage(chat_id,'Iniciada la deteccion de los PIRs') ## Envia un mensaje por Telegram
            ## LOG - deja registro del inicio
            log = open("log.txt", "w")
            log.write('PIR: Start at ' + time.ctime() + '\n')
            log.close()
            
        if command == '/stop': ## Para el py de la deteccion de movimiento
            os.system('pkill -9 -f pir.py &') ## este comando hay que revisarlo
            bot.sendMessage(chat_id,'Detenida la deteccion de los PIRs') ## Envia un mensaje por Telegram
            ## LOG - deja registro del "apagado" de la deteccion de movimiento
            log = open("log.txt", "w")
            log.write('PIR: Stop at ' + time.ctime() + '\n')
            log.close()

    else: ## Cuando se activa el bloqueo para que solo lo use el dueño y lo intenta usar otra persona
        bot.sendMessage(chat_id,'Sal de aqui maldito bastardo !') ## Envia un mensaje por Telegram
        ## LOG - deja registro
        log = open("log.txt", "w")
        log.write(chat_id + ' intento usar el bot. ( ' + time.ctime() + ' )\n' )
        log.close()

bot = telepot.Bot('--TOKEN--') ## Poner el TOKEN del bot
bot.message_loop(handle)

##LOG - Deja registro de que se inicio el programa
log = open("log.txt", "w")
log.write('Iniciando... [ ' + time.ctime() + ' ]\n')
log.close()

while 1:
    try:
        time.sleep(0.5)

    except KeyboardInterrupt:
        print('\n Program interrupted')
        GPIO.cleanup()
        exit()
