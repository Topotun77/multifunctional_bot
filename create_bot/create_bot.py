import os

import telebot

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)
