import io

import telebot
from PIL import Image, ImageOps
from telebot.types import Message, CallbackQuery

from settings import user_states
from .image_utl import (pixelate_image, image_to_ascii, convert_to_heatmap, grayscale,
                        convert_to_heatmap_v2, resize_for_sticker)


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


def send_image(message: Message, bot: telebot.TeleBot, image: Image.Image):
    """
    Отправить измененное изображение
    :param message: Message
    :param bot: telebot.TeleBot
    :param image: Изображение для отправки
    :return: io.BytesIO
    """
    output_stream = io.BytesIO()
    image.save(output_stream, format='JPEG')
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def pixelate_and_send(message: Message, bot: telebot.TeleBot, pixel_size=20):
    """
    Пикселизует изображение и отправляет его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    pixelated = pixelate_image(image, pixel_size=pixel_size)

    send_image(message, bot, pixelated)


def mirror_and_send(message: Message, bot: telebot.TeleBot, method: Image.Transpose = 1):
    """
    Отражает изображение и отправляет его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    mirror = image.transpose(method=method)

    send_image(message, bot, mirror)


def invert_and_send(message: Message, bot: telebot.TeleBot):
    """
    Инвертирует цвета изображения и отправляет его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    invert = ImageOps.invert(image)

    send_image(message, bot, invert)


def heatmap_and_send(message: Message, bot: telebot.TeleBot):
    """
    Преобразует в тепловую карту изображение и отправляет его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    heatmap = convert_to_heatmap(image)

    send_image(message, bot, heatmap)


def heatmap_v2_and_send(message: Message, bot: telebot.TeleBot):
    """
    Преобразует в тепловую карту изображение и отправляет его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    heatmap = convert_to_heatmap_v2(image)

    send_image(message, bot, heatmap)


def grayscale_and_send(message: Message, bot: telebot.TeleBot):
    """
    Преобразует в тепловую карту изображение и отправляет его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    heatmap = grayscale(image)

    send_image(message, bot, heatmap)


def solarize_and_send(message: Message, bot: telebot.TeleBot):
    """
    Соляризация изображения и отправка его обратно пользователю.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    solarize = ImageOps.solarize(image)

    send_image(message, bot, solarize)


def sticker_and_send(message: Message, bot: telebot.TeleBot):
    """
    Стикер из изображения.
    """
    image_stream = get_image(message, bot)

    image = Image.open(image_stream)
    sticker = resize_for_sticker(image)

    # send_image(message, bot, sticker)
    output_stream = io.BytesIO()
    sticker.save(output_stream, format='PNG')
    output_stream.seek(0)
    bot.send_sticker(message.chat.id, output_stream)


def ascii_and_send(call: CallbackQuery, bot: telebot.TeleBot):
    """
    Преобразует изображение в ASCII-арт и отправляет результат в виде текстового сообщения
    """
    image_stream = get_image(call.message, bot)

    ascii_art = image_to_ascii(image_stream, ascii_ch=user_states[call.message.chat.id]['ascii'])
    bot.send_message(call.message.chat.id, f"```\n{ascii_art}\n```", parse_mode='MarkdownV2')


