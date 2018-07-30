#
#	Telegram: @fedex6
#
#---------------------#

## Basic imports & configuration
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
import random

## Iniciar los  indicadores leds
os.system('python pys/leds.py &')

def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    usuario = msg['from']['username']
    
    ## LOG
    log = open("log.txt", "a") ##Abrir el log al principio

    if usuario == name_owner : ## para que lo usen ciertos usuarios (configuracion.py)
        ## Comandos declarados en el bot
        if command == '/iniciar': ## Inicia la deteccion de movimiento
            os.system('python pys/pir.py &') ## Inicia los PIR
            os.system('python pys/puertas.py &') ## Inicia las detecciones de puertas abiertas
            bot.sendMessage(chat_id,'Iniciada la deteccion de los PIRs y Puertas abiertas') ## Envia un mensaje por Telegram
            log.write('[ ' + time.ctime() + ' ] >>> PIR & Puertas: Started by ' + usuario + '\n') ## Log
            
        if command == '/stop': ## Para el py de la deteccion de movimiento
            os.system('pkill -9 -f pir.py &') ## este comando hay que revisarlo
            os.system('pkill -9 -f puertas.py &') ## Finaliza la deteccion de puertas abiertas
            bot.sendMessage(chat_id,'Detenida la deteccion de los PIRs y Puertas abiertas') ## Envia un mensaje por Telegram            
            log.write('[ ' + time.ctime() + ' ] >>> PIR & Puertas: Stoped by ' + usuario + '\n') ## Log
        
        ## Encender los leds
        if command == '/leds_on':
            os.system('python pys/leds.py &')
            bot.sendMessage(chat_id, 'Encendidos los Leds')
            log.write('[ ' + time.ctime() + ' ] >>> Leds: Encendidos por ' + usuario + '\n') ## Escribe el log de que se encendieron los leds

        ## Apagar los leds
        if command == '/leds_off':
            os.system('pkill -9 -f leds.py &')
            bot.sendMessage(chat_id, 'Se apagaron los Leds')
            log.write('[ ' + time.ctime() + ' ] >>>Leds: Apagados por ' + usuario + '\n') ## Escribe el log de que se apagaron los leds

        ## Comandos varios 
        if command =='/roll': ## Es solo de prueba, para ver si funciona el bot
            bot.sendMessage(chat_id, random.randint(1, 6))

        ## Comandos para Conocer chat_id y username para bloquear apps a 3ros
        if command == '/id': ## Devuelve el numero de id del chat, para luego configurar para que solo lo use el dueno [probar otros metodos]
            bot.sendMessage(chat_id, chat_id)

    else: ## Cuando se activa el bloqueo para que solo lo use el dueno y lo intenta usar otra persona
        bot.sendMessage(chat_id,'Sal de aqui maldito bastardo !') ## Envia un mensaje por Telegram
        log.write('[ ' + time.ctime() + ' ] >>> ' + usuario + ' intento usar el bot. || ' + command + '\n' ) ## Registro de quien quiso usar el bot, y que comando envio

    ## LOG
    log.close() ## Cierra el archivo de log

bot = telepot.Bot(token) ## Poner el Token del bot en configuracion.py
bot.message_loop(handle)

##LOG - Deja registro de que se inicio el programa
log = open("log.txt", "a")
log.write('[ ' + time.ctime() + ' ] >>> Starting...\n')
log.close()

while 1:
    try:
        time.sleep(0.5)

    except KeyboardInterrupt:
        ##LOG - Deja registro de que se freno el programa
        log = open("log.txt", "a")
        log.write('[ ' + time.ctime() + ' ] >>> Stoping...\n')
        log.close()
        print('\n Program interrupted')
        exit()