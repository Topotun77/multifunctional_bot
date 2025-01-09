import io

from PIL import Image
from telebot.types import Message, CallbackQuery

from settings import user_states, ASCII_CHARS
from .image_utl import pixelate_image, image_to_ascii


def pixelate_and_send(message: Message, bot):
    """
    Пикселизирует изображение и отправляет его обратно пользователю.
    """
    photo_id = user_states[message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    image = Image.open(image_stream)
    pixelated = pixelate_image(image, 20)

    output_stream = io.BytesIO()
    pixelated.save(output_stream, format='JPEG')
    output_stream.seek(0)
    bot.send_photo(message.chat.id, output_stream)


def ascii_step2(message: Message, call: CallbackQuery, bot):
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


def ascii_and_send(call: CallbackQuery, bot):
    """
    Преобразует изображение в ASCII-арт и отправляет результат в виде текстового сообщения
    """
    photo_id = user_states[call.message.chat.id]['photo']
    file_info = bot.get_file(photo_id)
    downloaded_file = bot.download_file(file_info.file_path)

    image_stream = io.BytesIO(downloaded_file)
    ascii_art = image_to_ascii(image_stream, ascii_ch=user_states[call.message.chat.id]['ascii'])
    bot.send_message(call.message.chat.id, f"```\n{ascii_art}\n```", parse_mode='MarkdownV2')


