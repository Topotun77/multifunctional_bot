import telebot
from telebot.types import CallbackQuery, Message

from keyboards.image_kb import get_options_keyboard, get_pixel_keyboard, get_mirror_keyboard
from settings import ASCII_TEXT, WELCOME_TEXT, IMAGE_TEXT, user_states, ASCII_CHARS, PIXEL_DICT, MIRROR_DICT
from utilities.processing_img import (pixelate_and_send, solarize_and_send, ascii_and_send, invert_and_send,
                                      mirror_and_send, heatmap_and_send, grayscale_and_send, heatmap_v2_and_send,
                                      sticker_and_send)

from create_bot.create_bot import bot


def callback_query(call: CallbackQuery):
    """
    Определяет действия в ответ на выбор пользователя
    bot.callback_query_handler(func=lambda call: True)
    """
    try:
        if call.data == 'pixelate':
            bot.send_message(call.message.chat.id, '👇 Выберите размер пикселя 👇', parse_mode='HTML',
                             reply_markup=get_pixel_keyboard())
        elif call.data == 'mirror':
            bot.send_message(call.message.chat.id, '👇 Выберите тип отражения 👇', parse_mode='HTML',
                             reply_markup=get_mirror_keyboard())
        elif call.data == 'solarize':
            bot.answer_callback_query(call.id, 'Соляризация вашего изображения...')
            solarize_and_send(call.message, bot)
        elif call.data == 'ascii':
            msg = bot.send_message(call.message.chat.id, ASCII_TEXT, parse_mode='HTML')
            bot.register_next_step_handler(msg, ascii_step2, call, bot)
        elif call.data == 'invert':
            bot.answer_callback_query(call.id, 'Инверсия цветов вашего изображения...')
            invert_and_send(call.message, bot)
        elif call.data == 'heatmap':
            bot.answer_callback_query(call.id, 'Преобразование в тепловую карту...')
            heatmap_and_send(call.message, bot)
        elif call.data == 'heatmap_v2':
            bot.answer_callback_query(call.id, 'Преобразование в тепловую карту...')
            heatmap_v2_and_send(call.message, bot)
        elif call.data == 'grayscale':
            bot.answer_callback_query(call.id, 'Преобразование градации серого...')
            grayscale_and_send(call.message, bot)
        elif call.data == 'sticker':
            bot.answer_callback_query(call.id, 'Формирование стикера...')
            sticker_and_send(call.message, bot)
    except Exception as er:
        bot.send_message(call.message.chat.id, 'Ошибка. Начните все сначала.')
        raise


def pixel_query(call: CallbackQuery):
    """
    Определяет размер пикселя
    """
    try:
        bot.answer_callback_query(call.id, 'Пикселизация вашего изображения...')
        # bot.delete_message(call.message.chat.id, call.message.id)
        pixelate_and_send(call.message, bot, PIXEL_DICT[call.data])
    except Exception as er:
        bot.send_message(call.message.chat.id, 'Ошибка. Начните все сначала.')


def mirror_query(call: CallbackQuery):
    """
    Определяет тип зеркального отражения
    """
    try:
        bot.answer_callback_query(call.id, 'Отражение вашего изображения...')
        # bot.delete_message(call.message.chat.id, call.message.id)
        mirror_and_send(call.message, bot, int(call.data[2:]))
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
    bot.message_handler(commands=['start', 'help'])
    """
    bot.reply_to(message, WELCOME_TEXT, parse_mode='HTML')


def handle_photo(message: Message):
    """
    Реагирует на изображения, отправляемые пользователями, и предлагает варианты обработки
    bot.message_handler(content_types=['photo'])
    """
    bot.reply_to(message, IMAGE_TEXT, reply_markup=get_options_keyboard())
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}
