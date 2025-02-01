# Многофункциональный ТГ-бот

Данный бот умеет генерировать картинки с помощью нейросети, работать с изображениями, 
применять к ним различные фильтры и делать ASCII-арт. Также он умеет подбрасывать монетку и 
выбирать случайную шутку или комплимент.

### История изменений:

• Бот может делать пикселизацию изображения и ASCII-арт на основе загруженного изображения.  
• Реализован функционал: пользователь может задавать свой набор символов для создания ASCII-арта из отправленного изображения.  
• Изменена структура модулей.  
• Добавлена инверсия изображения.  
• Добавлена соляризация изображения.  
• Добавлена возможность выбора размера пикселя для пикселизации. Список размеров пикселей хранится в файле настроек.  
• Добавлена возможность отражения изображения по горизонтали, вертикали и поворот изображения.  
• Преобразование в тепловую карту двумя методами.  
• Преобразование в градации серого.  
• Изменение размера изображения для стикера.  
• Стикер на прозрачном фоне.  
• Добавлена случайная шутка.  
• Добавлена генерация изображения через API Kandinsky.  
• После генерации изображения открывается клавиатура с возможными манипуляциями над изображением, 
аналогично загруженному изображению.  
• Стартовая инлайн-клавиатура заменена на reply-клавиатуру. 
Оставлена возможность использовать стартовую инлайн-клавиатуру.  
• Реализован выбор допуска прозрачного цвета для стикеров.  
• Добавлена возможность получить случайный комплимент.  
• Шутку и комплимент теперь можно получить не только из меню, но и по командам `/joke` и `/compliment` соответственно. 
Также добавлена команда `/gen_image` для генерации изображения.  
• Добавлена команда отмены при генерации изображения, если пользователь передумал что-то генерировать.  
• Реализован перезапуск бота в случае ошибки в его работе.  
• Реализована игра "Подбрасывание монетки". Выдает случайным образом значения "Орел" или "Решка".  

### Скриншот начала работы бота:
![img01](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n001.JPG?raw=true)
### Генерация изображения через API-Kandinsky:
![img12](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n014.JPG?raw=true)
### Обработка сгенерированного изображения:
![img13](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n015.JPG?raw=true)
### Выбор допусков по прозрачному фону для стикера:
![img14](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n017.JPG?raw=true)
![img15](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n018.JPG?raw=true)
### Пикселизация изображения с выбором размера пикселя:
![img02](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n002.JPG?raw=true)
### Преобразование в ASCII-арт:
![img03](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n003.JPG?raw=true)
### Инверсия изображения:
![img04](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n004.JPG?raw=true)
### Соляризация изображения:
![img05](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n005.JPG?raw=true)
### Отражение изображения по вертикали:
![img06](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n006.JPG?raw=true)
### Поворот изображения на 90 градусов:
![img07](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n007.JPG?raw=true)
### Тепловая карта:
![img08](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n010.JPG?raw=true)
### Тепловая карта версии 2:
![img09](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n011.JPG?raw=true)
### Градации серого:
![img10](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n009.JPG?raw=true)
### Стикер на прозрачном фоне:
![img11](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n012.JPG?raw=true)
### Случайная шутка и случайный комплимент:
![img16](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n016.JPG?raw=true)
### Игра подбрасывание монетки:
![img17](https://github.com/Topotun77/multifunctional_bot/blob/master/ScreenShots/n019.JPG?raw=true)


## Для запуска:
1. Установите все необходимые зависимости, выполнив команду:  
```
pip install -r requirements.txt
```
2. Настройте переменные окружения. Вам нужно определить следующие значения:
- `TOKEN` - токен для доступа к Вашему телеграм-боту. 
Его можно получить здесь: https://t.me/BotFather
- `API_KEY` и `SECRET_KEY` - API-ключи доступа к сервису Kandinsky. 
Для получения ключей нужно зарегистрироваться на [Fusion Brain](https://fusionbrain.ai/)
3. Запустить бота командой:
```
python main.py
```
