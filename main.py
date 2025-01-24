import time
from telebot import apihelper

from handlers.register_handler import register_handlers
from create_bot.create_bot import bot


register_handlers(bot)


if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(f'Connection Error: {e.args}')
            time.sleep(30)
            print('Попытка перезапустить бота...')
