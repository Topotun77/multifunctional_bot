from telebot import types


def get_reply_keyboard_from_dict(dict_kb: dict) -> types.ReplyKeyboardMarkup:
    """
    Создает меню-клавиатуру с кнопками из словаря dict_kb
    :param dict_kb: Словарь с клавиатурой
    :return: Клавиатура ReplyKeyboardMarkup
    """
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    list_key = []
    for k, v in dict_kb.items():
        list_key.append(types.KeyboardButton(v))
    keyboard.add(*list_key)
    return keyboard


def get_inline_keyboard_from_dict(dict_kb: dict) -> types.InlineKeyboardMarkup:
    """
    Создает инлайн клавиатуру с кнопками из словаря dict_kb
    :param dict_kb: Словарь с клавиатурой
    :return: Клавиатура InlineKeyboardMarkup
    """
    keyboard = types.InlineKeyboardMarkup()
    list_key = []
    for k, v in dict_kb.items():
        list_key.append(types.InlineKeyboardButton(v, callback_data=k))
    keyboard.add(*list_key)
    return keyboard