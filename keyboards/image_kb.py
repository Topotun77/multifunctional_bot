from telebot import types
from settings import PIXEL_DICT, MIRROR_DICT


def get_options_keyboard():
    """
    Создает клавиатуру с кнопками для выбора пользователем, как обработать изображение
    :return: Клавиатура InlineKeyboardMarkup
    """
    keyboard = types.InlineKeyboardMarkup()
    pixelate_btn = types.InlineKeyboardButton("Пикселизация", callback_data="pixelate")
    solarize_btn = types.InlineKeyboardButton("Соляризация", callback_data="solarize")
    ascii_btn = types.InlineKeyboardButton("ASCII-Арт", callback_data="ascii")
    invert_colors_btn = types.InlineKeyboardButton("Инвертировать", callback_data="invert")
    mirror_btn = types.InlineKeyboardButton("Отразить", callback_data="mirror")
    keyboard.add(pixelate_btn, ascii_btn, invert_colors_btn, solarize_btn, mirror_btn)
    return keyboard


def get_pixel_keyboard_from_dict(dict_kb: dict) -> types.InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками из словаря dict_kb
    :param dict_kb: Словарь с клавиатурой
    :return: Клавиатура InlineKeyboardMarkup
    """
    keyboard = types.InlineKeyboardMarkup()
    list_key = []
    for k, v in dict_kb.items():
        list_key.append(types.InlineKeyboardButton(v, callback_data=k))
    keyboard.add(*list_key)
    return keyboard


def get_pixel_keyboard() -> types.InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для выбора размера пикселов.
    Данные берет из словаря PIXEL_DICT
    :return: Клавиатура InlineKeyboardMarkup
    """
    return get_pixel_keyboard_from_dict(PIXEL_DICT)


def get_mirror_keyboard() -> types.InlineKeyboardMarkup:
    """
    Создает клавиатуру с кнопками для выбора типа отражения.
    Данные берет из словаря MIRROR_DICT
    :return: Клавиатура InlineKeyboardMarkup
    """
    return get_pixel_keyboard_from_dict(MIRROR_DICT)
