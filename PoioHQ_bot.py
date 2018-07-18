#
#	Telegram: @fedex6
#
#---------------------#

#####################
import os
import sys
import time
import datetime
import random
import telepot
#####################


def handle(msg):
    chat_id = msg['chat']['id']
    command = msg['text']
    usuario = msg['from']['username']
    
    ## LOG
    log = open("log.txt", "a") ##Abrir el log al principio

    if usuario == '-- USER --' : ## para que lo usen ciertos usuarios
        ## Comandos declarados en el bot
        if command == '/iniciar': ## Inicia la deteccion de movimiento
            os.system('python pys/pir.py &')
            bot.sendMessage(chat_id,'Iniciada la deteccion de los PIRs') ## Envia un mensaje por Telegram
            log.write('[ ' + time.ctime() + ' ] >>> PIR: Started by ' + usuario + '\n') ## Log
            
        if command == '/stop': ## Para el py de la deteccion de movimiento
            os.system('pkill -9 -f pir.py &') ## este comando hay que revisarlo
            bot.sendMessage(chat_id,'Detenida la deteccion de los PIRs') ## Envia un mensaje por Telegram            
            log.write('[ ' + time.ctime() + ' ] >>> PIR: Stoped by ' + usuario + '\n') ## Log

        ## Comandos varios 
        if command =='/roll': ## Es solo de prueba, para ver si funciona el bot
            bot.sendMessage(chat_id, random.randint(1, 6))

        ## Comandos para Conocer chat_id y username para bloquear apps a 3ros
        if command == '/id': ## Devuelve el numero de id del chat, para luego configurar para que solo lo use el dueno [probar otros metodos]
            bot.sendMessage(chat_id, chat_id)

        if command == '/user': ## obtener el usuario
            bot.sendMessage(chat_id, usuario)

    else: ## Cuando se activa el bloqueo para que solo lo use el dueno y lo intenta usar otra persona
        bot.sendMessage(chat_id,'Sal de aqui maldito bastardo !') ## Envia un mensaje por Telegram
        log.write('[ ' + time.ctime() + ' ] >>> ' + usuario + ' intento usar el bot. || ' + command + '\n' ) ## Registro de quien quiso usar el bot, y que comando envio

    ## LOG
    log.close() ## Cierra el archivo de log

bot = telepot.Bot('-- TOKEN --') ## Poner el Token del bot
bot.message_loop(handle)

##LOG - Deja registro de que se inicio el programa
log = open("log.txt", "a")
log.write('[ ' + time.ctime() + ' ] >>> Starting...\n')
log.close()

while 1:
    try:
        time.sleep(0.5)

    except KeyboardInterrupt:
        ##LOG - Deja registro de que se inicio el programa
        log = open("log.txt", "a")
        log.write('[ ' + time.ctime() + ' ] >>> Stoping...\n')
        log.close()
        print('\n Program interrupted')
        exit()
