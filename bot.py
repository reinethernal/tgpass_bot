#!/usr/bin/python
# -*- coding: utf-8 -*-
import config   # config file
import telegram
import os
import subprocess
import sys
import shlex
import datetime
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


def start(bot, update):
    if update.message.from_user.username not in config['users']:
        bot.sendMessage(update.message.chat_id, text="Sorry, you are not in the list")
        return

        bot.sendMessage(
        bot.update.message.chat_id,
        parse_mode="Markdown",
        text=(
            "Куку!\n"
            "Напишите */getpass* чтобы получить пароль,\n"
            "например */getpass имяпк ' 'чтобы получить пароль от нужного компа)"
        )
    )


def help(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text='''
   Введите /getpass* чтобы получить пароль."
            ''')

def getpass2(bot, update):
    sent = bot.send_message(message.chat.id, 'Имя пк?')
    bot.register_next_step_handler(sent, pcname)

#def gnom (sent, pcname, passes):
#    for file in glob.glob('*.pass'):
#    print 'DEBUG: file=>{0}<'.format(file)
#    with open(file) as f:
#        contents = f.read()
#    if 'struct' in contents:
#        print file

def gnom(sent, pcname, passes):
    with open("passes.txt") as f:
        for line in f:
            if pcname in line:
                print (line)
            else:
                print ("Нет такого")


def getpass(bot, chat_id):
    	bot.sendMessage(
	bot.update.message.chat_id,
	text=(gnom)
	)



dispatcher.add_handler(CommandHandler('help', help))
dispatcher.add_handler(CommandHandler('getpass', getpass))
dispatcher.add_handler(CommandHandler('start', start))
dispatcher.add_handler(CommandHandler('getpass2', getpass2))
dispatcher.add_handler(CommandHandler('gnom', gnom))



updater.start_polling()

