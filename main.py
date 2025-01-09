import os
import telebot
from telebot.types import Message, CallbackQuery

from keyboards.image_kb import get_options_keyboard
from settings import WELCOME_TEXT, IMAGE_TEXT, ASCII_TEXT, user_states
from utilities.processing_img import pixelate_and_send, ascii_step2

TOKEN = os.environ.get('TOKEN')
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message: Message):
    """ Обработчик приветствия """
    bot.reply_to(message, WELCOME_TEXT)


@bot.message_handler(content_types=['photo'])
def handle_photo(message: Message):
    """ Реагирует на изображения, отправляемые пользователем, и предлагает варианты обработки """

    bot.reply_to(message, IMAGE_TEXT, reply_markup=get_options_keyboard())
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call: CallbackQuery):
    """ Определяет действия в ответ на выбор пользователя """

    try:
        if call.data == 'pixelate':
            bot.answer_callback_query(call.id, 'Пикселизация вашего изображения...')
            pixelate_and_send(call.message, bot)
        elif call.data == 'ascii':
            msg = bot.send_message(call.message.chat.id, ASCII_TEXT, parse_mode='HTML')
            bot.register_next_step_handler(msg, ascii_step2, call, bot)
    except Exception as er:
        bot.send_message(call.message.chat.id, 'Ошибка. Начните все сначала.')


bot.polling(none_stop=True)
