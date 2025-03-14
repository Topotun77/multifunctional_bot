from PIL import Image, ImageOps
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


def grayscale(image: Image.Image) -> Image.Image:
    """ Конвертирование изображения в градации серого """
    return image.convert("L")


def transparent(image: Image.Image, tp_pixel=None, allowance=2) -> Image.Image:
    """
    Устанавливаем прозрачный фон
    :param image: Изображение для обработки
    :param tp_pixel: Прозрачный пиксель. По умолчанию левый верхний угол
    :param allowance: допуск разброса по прозрачному цвету
    :return: Обработанное изображение - стикер Image
    """
    def is_transparent(pixel) -> bool:
        """
        Проверка на близость к прозрачному цвету
        :param pixel: Пиксель для проверки
        :return: Истина/ложь
        """
        for i in range(3):
            if abs(tp_pixel[i] - pixel[i]) > allowance:
                return False
        return True

    rgba = image.convert("RGBA")
    datas = rgba.getdata()

    # Прозрачный пиксел, если не указан, то верхний левый пиксел
    if not tp_pixel:
        tp_pixel = datas[0]

    newData = []
    for item in datas:
        if is_transparent(item):
            # Меняем цвет пикселя на прозрачный
            newData.append((255, 255, 255, 0))
        else:
            newData.append(item)

    rgba.putdata(newData)
    return rgba


def image_to_ascii(image_stream, ascii_ch=ASCII_CHARS, new_width=40) -> str:
    """
    Преобразование изображение в ASCII-арт
    :param image_stream: Исходное изображение
    :param new_width: Ширина ASCII-арта в символах
    :param ascii_ch: Набор символов для преобразования в ASCII-арт
    :return: Полученный ASCII-арт
    """
    # Переводим в оттенки серого
    image = grayscale(Image.open(image_stream))

    # меняем размер сохраняя отношение сторон
    img_resized = resize_image(image, new_width, proportion=0.55)

    # Конвертирует пиксели изображения в градациях серого в строку ASCII-символов
    img_str = pixels_to_ascii(img_resized, ascii_ch)
    img_width = img_resized.width

    # Рассчитываем количество строк ASCII-арта
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
    # Уменьшаем изображение в pixel_size раз
    image = image.resize(
        (image.size[0] // pixel_size, image.size[1] // pixel_size),
        Image.NEAREST
    )

    # Увеличиваем изображение в pixel_size раз
    image = image.resize(
        (image.size[0] * pixel_size, image.size[1] * pixel_size),
        Image.NEAREST
    )
    return image


def convert_to_heatmap(image: Image.Image) -> Image.Image:
    """
    Конвертация в тепловую карту.
    Преобразует изображение в оттенки серого, затем применяет метод ImageOps.colorize.
    :param image: Исходное изображение
    :return: Преобразованное изображение
    """
    # Переводим в оттенки серого
    image = image.convert('L')

    # Создать новую пустую картинку для тепловой карты
    heatmap = Image.new('RGB', image.size)
    pixels = heatmap.load()

    # Определить цветовую палитру тепловой карты
    colors = [
        (0, 0, 128),
        (0, 0, 255),
        (0, 255, 0),
        (255, 255, 0),
        (255, 165, 0),
        (255, 0, 0)
    ]

    # Перебрать каждый пиксель исходного изображения
    for x in range(image.width):
        for y in range(image.height):
            # Получить яркость текущего пикселя
            brightness = image.getpixel((x, y))

            # Отнормировать яркость к диапазону [0, 1]
            normalized_brightness = brightness / 255

            # Найти соответствующий индекс в цветовой палитре
            index = int(normalized_brightness * (len(colors) - 1))

            # Установить цвет пикселя в новой картинке
            pixels[x, y] = colors[index]

    return heatmap


def convert_to_heatmap_v2(image: Image.Image) -> Image.Image:
    """
    Конвертация в тепловую карту. Вариант 2.
    Преобразует изображение в оттенки серого, затем применяет метод ImageOps.colorize.
    :param image: Исходное изображение
    :return: Преобразованное изображение
    """
    # Переводим в оттенки серого
    image = image.convert('L')

    # Создаем тепловую карту (синий, желтый, красный)
    image = ImageOps.colorize(image, black=(0, 0, 255), white=(255, 0, 0), mid=(255, 255, 0))

    return image


def resize_for_sticker(image: Image.Image, max_pixel=512, allowance=2) -> Image.Image:
    """
    Изменяет размер изображения, сохраняя пропорции, чтобы его максимальное измерение
    не превышало заданного максимума (по умолчанию 512 пикселей).
    :param image: Исходное изображение
    :param max_pixel: Максимальное измерение в пикселях
    :param allowance: допуск разброса по прозрачному цвету
    :return: Преобразованное изображение
    """
    # Меняем размер
    max_size = max(image.width, image.height)
    if max_size > max_pixel:
        # Новый размер
        image = resize_image(image, round(image.width * (max_pixel / max_size)))

    # Делаем прозрачный фон
    image = transparent(image, allowance=allowance)

    return image
