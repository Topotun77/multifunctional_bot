from telebot import types
from settings import PIXEL_DICT, MIRROR_DICT, START_KB_DICT
from .generate_kb import get_inline_keyboard_from_dict as get_inline_kb


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
    heatmap_btn = types.InlineKeyboardButton("Тепловая карта", callback_data="heatmap")
    heatmap_v2_btn = types.InlineKeyboardButton("Тепловая карта V2", callback_data="heatmap_v2")
    grayscale_btn = types.InlineKeyboardButton("Градации серого", callback_data="grayscale")
    sticker_btn = types.InlineKeyboardButton("Стикер", callback_data="sticker")
    keyboard.add(pixelate_btn, ascii_btn, invert_colors_btn, solarize_btn, mirror_btn,
                 grayscale_btn, heatmap_btn, heatmap_v2_btn, sticker_btn)
    return keyboard
