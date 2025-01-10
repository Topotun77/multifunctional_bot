import telebot

from handlers.image_handlers import send_welcome, handle_photo, callback_query


def register_handlers(bot: telebot.TeleBot):
    bot.message_handler(commands=['start', 'help'])(send_welcome)
    bot.message_handler(content_types=['photo'])(handle_photo)
    bot.callback_query_handler(func=lambda call: True)(callback_query)

