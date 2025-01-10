import telebot
from telebot.types import CallbackQuery, Message

from keyboards.image_kb import get_options_keyboard
from settings import ASCII_TEXT, WELCOME_TEXT, IMAGE_TEXT, user_states, ASCII_CHARS
from utilities.processing_img import pixelate_and_send, ascii_and_send, invert_and_send

from create_bot.create_bot import bot


def callback_query(call: CallbackQuery):
    """
    Определяет действия в ответ на выбор пользователя
    bot.callback_query_handler(func=lambda call: True)
    """
    try:
        if call.data == 'pixelate':
            bot.answer_callback_query(call.id, 'Пикселизация вашего изображения...')
            pixelate_and_send(call.message, bot)
        elif call.data == 'ascii':
            msg = bot.send_message(call.message.chat.id, ASCII_TEXT, parse_mode='HTML')
            bot.register_next_step_handler(msg, ascii_step2, call, bot)
        elif call.data == 'invert':
            bot.answer_callback_query(call.id, 'Инверсия цветов вашего изображения...')
            invert_and_send(call.message, bot)
    except Exception as er:
        bot.send_message(call.message.chat.id, 'Ошибка. Начните все сначала.')


def ascii_step2(message: Message, call: CallbackQuery, bot: telebot.TeleBot):
    """
    Шаг 2: обработка запроса у пользователя набора символов для ASCII-арта.
    """
    bot.send_message(call.message.chat.id, 'Преобразование вашего изображения в формат ASCII...')

    if len(message.text) < 2:
        ascii_ch = ASCII_CHARS
    else:
        ascii_ch = message.text
    user_states[call.message.chat.id]['ascii'] = ascii_ch
    ascii_and_send(call, bot)


def send_welcome(message: Message):
    """
    Обработчик приветствия
    commands=['start', 'help']
    """
    bot.reply_to(message, WELCOME_TEXT, parse_mode='HTML')


def handle_photo(message: Message):
    """
    Реагирует на изображения, отправляемые пользователями, и предлагает варианты обработки
    content_types=['photo']
    """
    bot.reply_to(message, IMAGE_TEXT, reply_markup=get_options_keyboard())
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}
