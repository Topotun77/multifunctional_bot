from random import randint, choice
import telebot
from telebot.types import CallbackQuery, Message

from keyboards.image_kb import get_options_keyboard
from keyboards.generate_kb import get_reply_keyboard_from_dict, get_inline_keyboard_from_dict
from settings import (
    ASCII_TEXT, WELCOME_TEXT, IMAGE_TEXT, user_states, ASCII_CHARS, PIXEL_DICT, JOKES,
    IMAGE_GEN_TEXT, ERROR_TEXT, START_KB_DICT, MIRROR_DICT, TRANSPARENT_DICT, TRANSPARENT_TEXT,
    UNDERSTAND_TEXT, COMPLIMENTS, FRAME_COMPLIMENTS, CANCEL_TEXT, COIN_DICT
)
from utilities.processing_img import (
    pixelate_and_send, solarize_and_send, ascii_and_send, invert_and_send, mirror_and_send,
    heatmap_and_send, grayscale_and_send, heatmap_v2_and_send, sticker_and_send, generate_and_send
)

from create_bot.create_bot import bot


def start_query(call: CallbackQuery | Message):
    """
    Определяет действия в ответ на выбор пользователя при старте
    bot.callback_query_handler(func=lambda call: call.data in START_KB_DICT)(start_query)
    """
    # Для разрешения проблемы типов данных Reply и Inline клавиатур
    if type(call) == CallbackQuery:
        message=call.message
        text=START_KB_DICT[call.data]
    else:
        message=call
        text=message.text
        # В случае, если была команда, начинающаяся со '/'
        if text[0] == '/':
            text = START_KB_DICT[text[1:]]
    try:
        if text == START_KB_DICT['joke']:
            bot.send_message(message.chat.id, text=JOKES[randint(0, len(JOKES)-1)],
                             parse_mode='HTML')
        elif text == START_KB_DICT['compliment']:
            comp = (FRAME_COMPLIMENTS + '<b>' +
                    COMPLIMENTS[randint(0, len(COMPLIMENTS) - 1)] +
                    '</b>' + FRAME_COMPLIMENTS)
            bot.send_message(message.chat.id, text=comp, parse_mode='HTML')
        elif text == START_KB_DICT['coin']:
            coin = f'Вам выпало: <b>{choice(COIN_DICT)}</b>'
            bot.send_message(message.chat.id, text=coin, parse_mode='HTML')
        elif text == START_KB_DICT['gen_image']:
            msg = bot.send_message(message.chat.id, IMAGE_GEN_TEXT, parse_mode='HTML')
            bot.register_next_step_handler(msg, gen_step2, message, bot)
    except Exception as er:
        bot.send_message(message.chat.id, ERROR_TEXT)


def gen_step2(message: Message, msg: Message, bot: telebot.TeleBot):
    """
    Шаг 2: обработка запроса текста для генерации картинки.
    """
    if message.text == '/cancel':
        bot.send_message(msg.chat.id, CANCEL_TEXT, parse_mode='HTML')
        return
    bot.send_message(msg.chat.id, '⏳ <b>Идет генерация картинки.</b>\nЭто может занять несколько минут.',
                     parse_mode='HTML')
    generate_and_send(message, bot)


def callback_query(call: CallbackQuery):
    """
    Определяет действия в ответ на выбор пользователя
    bot.callback_query_handler(func=lambda call: True)
    """
    try:
        if call.data == 'pixelate':
            bot.send_message(call.message.chat.id, '👇 Выберите размер пикселя 👇', parse_mode='HTML',
                             reply_markup=get_inline_keyboard_from_dict(PIXEL_DICT))
        elif call.data == 'mirror':
            bot.send_message(call.message.chat.id, '👇 Выберите тип отражения 👇', parse_mode='HTML',
                             reply_markup=get_inline_keyboard_from_dict(MIRROR_DICT))
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
            bot.send_message(
                chat_id=call.message.chat.id,
                text=TRANSPARENT_TEXT,
                parse_mode='HTML',
                reply_markup=get_inline_keyboard_from_dict(TRANSPARENT_DICT)
            )
    except Exception as er:
        bot.send_message(call.message.chat.id, ERROR_TEXT)


def pixel_query(call: CallbackQuery):
    """
    Определяет размер пикселя
    bot.callback_query_handler(func=lambda call: call.data in PIXEL_DICT)(pixel_query)
    """
    try:
        bot.answer_callback_query(call.id, 'Пикселизация вашего изображения...')
        # bot.delete_message(call.message.chat.id, call.message.id)
        pixelate_and_send(call.message, bot, PIXEL_DICT[call.data])
    except Exception as er:
        bot.send_message(call.message.chat.id, ERROR_TEXT)


def mirror_query(call: CallbackQuery):
    """
    Определяет тип зеркального отражения
    bot.callback_query_handler(func=lambda call: call.data in MIRROR_DICT)(mirror_query)
    """
    try:
        bot.answer_callback_query(call.id, 'Отражение вашего изображения...')
        mirror_and_send(call.message, bot, int(call.data[2:]))
    except Exception as er:
        bot.send_message(call.message.chat.id, ERROR_TEXT)


def transparent_query(call: CallbackQuery):
    """
    Определяет размер допуска прозрачности фона
    bbot.callback_query_handler(func=lambda call: call.data in TRANSPARENT_DICT)(transparent_query)
    """
    try:
        bot.answer_callback_query(call.id, 'Формирование стикера...')
        sticker_and_send(call.message, bot, allowance=TRANSPARENT_DICT[call.data])
    except Exception as er:
        bot.send_message(call.message.chat.id, ERROR_TEXT)


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
    print(f'К нам пришел @{message.chat.username} ({message.chat.first_name})')
    bot.reply_to(message, WELCOME_TEXT, parse_mode='HTML', reply_markup=get_reply_keyboard_from_dict(START_KB_DICT))


def any_text(message: Message):
    """
    Обработчик приветствия
    bot.message_handler(commands=['start', 'help'])
    """
    print(f'К нам пришел @{message.chat.username} ({message.chat.first_name})')
    bot.reply_to(message, UNDERSTAND_TEXT, parse_mode='HTML', reply_markup=get_reply_keyboard_from_dict(START_KB_DICT))


def handle_photo(message: Message):
    """
    Реагирует на изображения, отправляемые пользователями, и предлагает варианты обработки
    bot.message_handler(content_types=['photo'])
    """
    bot.reply_to(message, IMAGE_TEXT, reply_markup=get_options_keyboard())
    user_states[message.chat.id] = {'photo': message.photo[-1].file_id}
