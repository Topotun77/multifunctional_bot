import telebot

from handlers.image_handlers import send_welcome, handle_photo, callback_query, pixel_query, mirror_query, start_query
from settings import PIXEL_DICT, MIRROR_DICT, START_KB_DICT


def register_handlers(bot: telebot.TeleBot):
    bot.message_handler(commands=['start', 'help'])(send_welcome)
    bot.message_handler(content_types=['photo'])(handle_photo)
    bot.callback_query_handler(func=lambda call: call.data in START_KB_DICT)(start_query)
    bot.callback_query_handler(func=lambda call: call.data in PIXEL_DICT)(pixel_query)
    bot.callback_query_handler(func=lambda call: call.data in MIRROR_DICT)(mirror_query)
    bot.callback_query_handler(func=lambda call: True)(callback_query)

