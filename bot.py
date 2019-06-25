#!/usr/bin/python3
import config   # config file
import telegram
import os
import subprocess
import sys
import shlex
import datetime
import glob
from subprocess import Popen, PIPE
from telegram.ext import CommandHandler
#'''модуль для перезагрузки (обновления) других модулей'''
from imp import reload
import codecs
# bot = telegram.Bot(token = config.token)
# Проверка бота
# print(bot.getMe())
import logging
from datetime import datetime




from telegram.ext import Updater
updater = Updater(token=config.token)
dispatcher = updater.dispatcher

# Enable logging
#logging.basicConfig(filename='/home/tgbot/bot.log', format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
#logger = logging.getLogger(__name__)


logfile = "/home/tgbot/bot.log"

def logString(s):
    f=open(logfile, "at")
    f.write( datetime.now().strftime("%d.%m.%y %H:%M:%S ")+  s +'\n')
    f.close()



def checkUser(bot,update):
    usname = update.message.from_user.username
    valid = usname in config.users

    if not valid:
       bot.sendMessage(update.message.chat_id, text="Sorry, you are not in the list")
       return False
    else: return True


def start(bot, update):
    print('starting...')
    if not checkUser(bot, update): return
    bot.sendMessage(  bot.update.message.chat_id,   parse_mode="Markdown",  text=" /getpass имяпк, чтобы получить пароль от нужного компа"  )


def help(bot, update):
    if not checkUser(bot, update): return
    print("help...")
    bot.sendMessage(chat_id=update.message.chat_id, text='Введите /getpass* чтобы получить пароль.')

def gp4(pcname):
    path="/mnt/passes/"
    with codecs.open(path+pcname+'.pass',encoding='cp866') as f:
       l=f.read().strip()
       return l [ l.find(':')+2:  ]


def getpass(bot, update):
    print('getpass....')
    if not checkUser(bot, update): 
       print('not checked..')
       logString('bad attempt for user '+update.message.from_user.username)
       return
    else:
       print('checked...')

    msg = update.message.text.split(' ')[1]
    print('msg: '+msg)
    logString('sending pass for pc '+msg+' to user ' +update.message.from_user.username)
    bot.send_message(chat_id=update.message.chat_id, text=gp4(msg))



dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('getpass', getpass))
dispatcher.add_handler(CommandHandler('start', start))



#print( gp4 ("462-0"));

#print(gp4('100-3'))

updater.start_polling()

