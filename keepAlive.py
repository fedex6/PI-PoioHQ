# -*- coding: utf-8 -*-
#
#   Telegram: @fedex6
#
#-------------------------------------------------------#

## Basic imports & configuration
import os
import sys
import time

## LOG
log = open("log.txt", "a") ##Abrir el log al principio

os.system('pkill -9 -f PoioHQ_bot &')
log.write('[ ' + time.ctime() + ' ] >>> BOT Stopped\n') ## Log

time.sleep(1)

os.system('python /home/pi/PoioHQ/PoioHQ_bot.py &')
log.write('[ ' + time.ctime() + ' ] >>> BOT Started\n') ## Log

log.close()
exit()