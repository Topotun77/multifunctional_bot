from handlers.register_handler import register_handlers
from create_bot.create_bot import bot


register_handlers(bot)


if __name__ == '__main__':
    bot.polling(none_stop=True)
