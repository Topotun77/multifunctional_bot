from telebot import types


def get_options_keyboard():
    """ Создает клавиатуру с кнопками для выбора пользователем, как обработать изображение """
    keyboard = types.InlineKeyboardMarkup()
    pixelate_btn = types.InlineKeyboardButton("Пикселизация", callback_data="pixelate")
    ascii_btn = types.InlineKeyboardButton("ASCII-Арт", callback_data="ascii")
    keyboard.add(pixelate_btn, ascii_btn)
    return keyboard

