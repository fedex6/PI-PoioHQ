#   
#   PoioHQ : Parser
#---------------------#

## Basic imports
import os
import sys
import time
import argparse
import datetime
import telepot

## Bot data
token       =   '-- TOKEN --'
chat_owner  =   '-- # of chat owner --'
name_owner  =   '-- name without @ of owner --'

## Others
import RPi.GPIO as GPIO

## Parser
parser = argparse.ArgumentParser()

## Argumentos
parser.add_argument("-a", "--activar", help="Activar un determinado sensor", action="store_true")
parser.add_argument("-d", "--desactivar", help="Desactivar un determinado sensor", action="store_true")
parser.add_argument("-s", "--status", help="Status un determinado sensor", action="store_true")

## Empieza el quilombo
args = parser.parse_args()

def handle(msg):
    chat_id = msg['chat']['id']
    command = split(' ', msg['text'], 1)
    usuario = msg['from']['username']

	if command[0] == args.activar:
		# Si hubiese un switch entre cosas seria mas facil
		### La idea es que el command[1] sea el sensor que quiere activar
		### Se podria hacer con botones, pero deberia aprender como recibir 
		### un msg, y esperar al siguiente para ejecutar lo que sigue

	if command[0] == args.desactivar:
		# Si hubiese un switch entre cosas seria mas facil
		### La idea es que el command[1] sea el sensor que quiere desactivar

	if command[0] == args.status:
		# Si hubiese un switch entre cosas seria mas facil
		### La idea es que el command[1] sea el sensor del que se quiere
		### saber el status

bot = telepot.Bot(token) ## Poner el Token del bot en configuracion.py
bot.message_loop(handle)

