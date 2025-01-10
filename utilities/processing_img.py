import io

import telebot
from PIL import Image, ImageOps
from telebot.types import Message, CallbackQuery

from settings import user_states
from .image_utl import pixelate_image, image_to_ascii


def get_image(message: Message, bot: telebot.TeleBot) -> io.BytesIO:
    """
    Взять загруженное изображение из user_states
    :param message: Message
    :param bot: telebot.TeleBot
    :return: io.BytesIO
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)
    image_stream = io.BytesIO(downloaded_file)
    return image_stream


def pixelate_and_send(message: Message, bot: telebot.TeleBot):
    """
    Пикселизует изображение и отправляет его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    pixelated = pixelate_image(image, 20)

    output_stream = io.BytesIO()
    pixelated.save(output_stream, format='JPEG')
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def invert_and_send(message: Message, bot: telebot.TeleBot):
    """
    Инвертирует цвета изображения и отправляет его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    invert = ImageOps.invert(image)

    output_stream = io.BytesIO()
    invert.save(output_stream, format='JPEG')
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def ascii_and_send(call: CallbackQuery, bot: telebot.TeleBot):
    """
    Преобразует изображение в ASCII-арт и отправляет результат в виде текстового сообщения
    """
    image_stream = get_image(call.message, bot)

    ascii_art = image_to_ascii(image_stream, ascii_ch=user_states[call.message.chat.id]['ascii'])
    bot.send_message(call.message.chat.id, f"```\n{ascii_art}\n```", parse_mode='MarkdownV2')


