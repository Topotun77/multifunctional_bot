from telebot import types


def get_options_keyboard():
    """ Создает клавиатуру с кнопками для выбора пользователем, как обработать изображение """
    keyboard = types.InlineKeyboardMarkup()
    pixelate_btn = types.InlineKeyboardButton("Пикселизация", callback_data="pixelate")
    ascii_btn = types.InlineKeyboardButton("ASCII-Арт", callback_data="ascii")
    invert_colors_btn = types.InlineKeyboardButton("Инвертировать", callback_data="invert")
    keyboard.add(pixelate_btn, ascii_btn, invert_colors_btn)
    return keyboard

