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
'''модуль для перезагрузки (обновления) других модулей'''
from imp import reload
# bot = telegram.Bot(token = config.token)
# Проверка бота
# print(bot.getMe())

from telegram.ext import Updater
updater = Updater(token=config.token)
dispatcher = updater.dispatcher


#Users = ['ReinEthernal']


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
    path="/home/zadmin/4/passwords/"
    with open(path+pcname+'.pass', 'r') as f:
          return f.read()


def getpass(bot, update):
    print('getpasss....')
    if not checkUser(bot, update): 
       print('not checked..')
       return
    else:
       print('checked...')

    msg = update.message.text.split(' ')[1]
    bot.send_message(chat_id=update.message.chat_id, text=gp4(msg))



dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('getpass', getpass))
dispatcher.add_handler(CommandHandler('start', start))



updater.start_polling()

