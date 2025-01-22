import telebot

from handlers.image_handlers import (
    send_welcome, handle_photo, callback_query, pixel_query, mirror_query, start_query, transparent_query, any_text
)
from settings import PIXEL_DICT, MIRROR_DICT, START_KB_DICT, TRANSPARENT_DICT
from utilities.image_utl import transparent


def register_handlers(bot: telebot.TeleBot):
    bot.message_handler(commands=['start', 'help'])(send_welcome)
    bot.message_handler(commands=[x for x in START_KB_DICT])(start_query)
    bot.message_handler(content_types=['photo'])(handle_photo)
    # Стартовая reply-клавиатура
    bot.message_handler(
        func=lambda message: message.text in [START_KB_DICT[x] for x in START_KB_DICT]
    )(start_query)
    # Стартовая inline-клавиатура
    bot.callback_query_handler(func=lambda call: call.data in START_KB_DICT)(start_query)
    bot.callback_query_handler(func=lambda call: call.data in PIXEL_DICT)(pixel_query)
    bot.callback_query_handler(func=lambda call: call.data in MIRROR_DICT)(mirror_query)
    bot.callback_query_handler(func=lambda call: call.data in TRANSPARENT_DICT)(transparent_query)
    bot.callback_query_handler(func=lambda call: True)(callback_query)
    bot.message_handler()(any_text)

