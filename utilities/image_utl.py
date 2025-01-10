from PIL import Image
from settings import ASCII_CHARS


def resize_image(image: Image.Image, new_width=100, proportion: float = 1) -> Image.Image:
    """
    Изменение размера изображения
    :param image: Исходное изображение
    :param new_width: Новая ширина изображения
    :param proportion: пропорции высоты и ширины
    :return: Измененное изображение
    """
    width, height = image.size
    ratio = height / float(width)
    new_height = round(new_width * ratio * proportion)
    return image.resize((new_width, new_height))


def grayify(image: Image.Image) -> Image.Image:
    """ Конвертирование изображения в градации серого """
    return image.convert("L")


def image_to_ascii(image_stream, ascii_ch=ASCII_CHARS, new_width=40) -> str:
    """
    Преобразование изображение в ASCII-арт
    :param image_stream: Исходное изображение
    :param new_width: Ширина ASCII-арта в символах
    :param ascii_ch: Набор символов для преобразования в ASCII-арт
    :return: Полученный ASCII-арт
    """
    # Переводим в оттенки серого
    image = grayify(Image.open(image_stream))

    # меняем размер сохраняя отношение сторон
    img_resized = resize_image(image, new_width, proportion=0.55)

    img_str = pixels_to_ascii(img_resized, ascii_ch)
    img_width = img_resized.width

    max_characters = 4000 - (new_width + 1)
    max_rows = max_characters // (new_width + 1)

    ascii_art = ""
    for i in range(0, min(max_rows * img_width, len(img_str)), img_width):
        ascii_art += img_str[i:i + img_width] + "\n"

    return ascii_art


def pixels_to_ascii(image: Image.Image, ascii_ch=ASCII_CHARS) -> str:
    """
    Конвертирует пиксели изображения в градациях серого в строку ASCII-символов,
    используя предопределенную строку ASCII_CHARS
    :param image: Исходное изображение в градациях серого.
    :param ascii_ch: Набор символов для преобразования в ASCII-арт
    :return: Строка символов ASCII.
    """
    pixels = image.getdata()

    characters = ""
    for pixel in pixels:
        characters += ascii_ch[pixel * len(ascii_ch) // 256]
    return characters


def pixelate_image(image: Image.Image, pixel_size: int) -> Image.Image:
    """
    Уменьшает изображение до размера, где один пиксель представляет большую область,
    затем увеличивает обратно, создавая пиксельный эффект.
    :param image: Исходное изображение
    :param pixel_size: размер пикселя
    :return: Преобразованное изображение
    """
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    return image

