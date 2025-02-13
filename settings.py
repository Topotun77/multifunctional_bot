from PIL.Image import Transpose

# Набор символов из которых составляем изображение (по умолчанию)
ASCII_CHARS = '@Odo*+=-. '

# Тексты для пользователя
WELCOME_TEXT = """<b>Привет!</b> 👋 
Я - многофункциональный бот!

Выберете действие из списка или пришлите мне изображение, и я предложу, что с ним можно сделать.

<b>А еще я знаю такие команды как:</b>
<b>/gen_image</b> - сгенерировать картинку
<b>/joke</b> - показать случайную шутку
<b>/compliment</b> - сделать случайный комплимент
<b>/coin</b> - игра "Орел или Решка"
"""

UNDERSTAND_TEXT = """Начните с команды /start"""

CANCEL_TEXT = '<b>Вы нажали отмену.</b>\nВыберите действие в меню или начните с команды /start'

IMAGE_TEXT = """У меня есть ваша фотография!
Пожалуйста, выберите, что Вы хотите с ней сделать?"""

ASCII_TEXT = f"""✍️ <b>Пожалуйста, введите набор символов для преобразования изображения в ASCII-арт.</b>
По умолчанию при вводе одного любого символа будет последовательность:
<pre>{ASCII_CHARS}</pre>"""

IMAGE_GEN_TEXT = f"""✍️ <b>Пожалуйста, введите текст запроса для генерации изображения.</b>
<i>Опишите подробно, что Вы хотите видеть на картинке.</i> 
Для отмены нажмите /cancel
"""

TRANSPARENT_TEXT = """<b>Пожалуйста, выберите размер поля допуска для прозрачного цвета фона.</b>
<i> -1 — нет прозрачного фона,</i> 
<i> 0 — прозрачный цвет точно соответствует цвету левого верхнего пикселя,</i>
<i> 1 — прозрачный цвет ±1 к цвету левого верхнего пикселя,</i> 
и т.д...
👇👇👇"""

ERROR_TEXT = """Ошибка. Начните все сначала. Например, с команды /start"""

# Тут будем хранить информацию о действиях пользователя
user_states = {}

# Словарь для стартовой клавиатуры
START_KB_DICT = {
    'gen_image': 'Сгенерировать картинку',
    'joke': 'Шутка',
    'compliment': 'Комплимент',
    'coin': 'Орел или Решка',
}

# Словарь для выбора результатов игры "Подбрасывание монеты"
COIN_DICT = ['Орел', 'Решка']

# Словарь размеров пикселя для клавиатуры
PIXEL_DICT = {
    'p_10': 10,
    'p_20': 20,
    'p_30': 30,
    'p_40': 40,
    'p_50': 50,
}

# Словарь размеров допусков прозрачности фона
TRANSPARENT_DICT = {
    'tr_-1': -1,
    'tr_0': 0,
    'tr_1': 1,
    'tr_2': 2,
    'tr_3': 3,
    'tr_5': 5,
    'tr_7': 7,
    'tr_10': 10,
    'tr_20': 15,
    'tr_30': 20,
    'tr_40': 30,
    'tr_50': 50,
    'tr_70': 70,
    'tr_100': 100,
    'tr_150': 150,
}

# Словарь методов отражения изображения для клавиатуры
MIRROR_DICT = {
    f'm_{Transpose.FLIP_LEFT_RIGHT}': 'Горизонтальное',
    f'm_{Transpose.FLIP_TOP_BOTTOM}': 'Вертикальное',
    f'm_{Transpose.ROTATE_90}': '90 градусов',
    f'm_{Transpose.ROTATE_180}': '180 градусов',
    f'm_{Transpose.ROTATE_270}': '270 градусов',
}

# Список шуток
JOKES = [
    'Ученые думают, что человек на 80% состоит из воды, в отличии от тигров и крокодилов… которые думают, '
    'что человек на 100% состоит из еды.',
    'Вашими бы устами да помолчать...',
    '— За что вас арестовали?\n— За взятку.\n— А как отпустили?\n— Вы тупой?',
    'Уважаемые жильцы! Завтра с 8:00 до 20:00 у вас будет совершенно легальная возможность не мыть посуду. '
    'Не благодарите! ',
    '— Мама, а если червяка разрезать, то его половинки будут дружить?\n— С тобой — нет.',
    '— Подсудимый, клянетесь ли вы говорить правду, только правду и ничего, кроме правды?\n'
    '— Клянусь, толстая женщина с усиками.',
    '— Мам, я красивая?\n— Спроси у своего парня лучше.\n— Какого парня?\n— Вот именно.',
    """Прошла акция «День без мата». 
❌ Полностью парализована работа всех автосервисов; 
❌ Застопорились все погрузочно—разгрузочные работы; 
❌ Хоккеисты не поняли тренера на установке перед матчем; 
❌ Местный трудовик умер на вдохе; 
❌ А обычные жители не знали что ответить на элементарный вопрос «Где?».""",
    'Девушка становится женщиной, когда впервые говорит: «Это хороший пакет, не выбрасывай!»',
    'Мяч еще летел в окно директора, а дети уже играли в прятки.',
    'Прошлой ночью не получилось вызвать такси до дома, так я зашел в кафе, заказал доставку '
    'на свой адрес и уехал вместе с водителем.',
    'Сбербанк отнес стоимость посещения мной платного туалета к категории "Развлечения и хобби". '
    'Вот сижу и думаю, это моё развлечение? Или моё хобби?',
    'Объявление: "Ищу высокого мужчину, чтобы помог снять тюль для стирки. Разовые отношения не '
    'интересуют - потом тюль нужно будет повесить обратно".',
    '  — Рабинович, а ви слышали, шо в будущем не будет денег? \n  — Да вы шо, и в будущем тоже?!',
    'Передача "Жди меня". \n  — Мой муж ушёл из дома 4 года назад. За это время я родила ему '
    'четверых детей. Имей совесть, Алёша. Вернись домой.',
    'Если человек, проходя по улице мимо кота, не говорит ему автоматически кс-кс, то я к '
    'такому человеку сразу отношусь настороженно. Он явно рептилоид, или жук-оборотень, или масон. '
    'Звуковое пингование случайных котов — единственнoe, что отличаeт человека от потусторонней '
    'сущности.',
    'Как определить, кто в дорогом отеле миллиардер, а кто обслуживающий персонал? \n'
    '  — Миллиардер ходит в мятой майке, шортах и шлёпках. А обслуживающий персонал - в '
    'выглаженных деловых костюмах, рубашках и галстуках.',
    '   Фотоальбом наших прабабушек:\n1928 — пошла в школу (1 фото)\n1938 — закончила школу '
    '(3 фото)\n1945 — окончила университет (1 фото)\n1946 — вышла замуж (3 фото).'
    '\n\n   Фотоальбом их правнучек:\n19:38 — пришла в кафе (28 фото)\n19:41 — принесли меню '
    '(19 фото)\n19:52 — принесли Цезарь (20 фото)\n19:56 — принесли отбивные (19 фото)'
    '\n19:58 — пошла в туалет пописять (80 фото)\n20:03 — выходя из туалета встретила '
    'подружку (52 фото)\n20:15 — принесли кофе и мороженку (38 фото)\n20:29 — принесли счет (11 фото)',
    'Весна - она как женщина. Кричит "Иду уже, иду", а сама ещё сидит в ванной с мокрой головой и ногти красит.',
    '- Книга получается хорошей, если автор действительно знает то, о чём пишет.\n- Фильм получается хорошим, '
    'если сценарист, режиссёр, актёры хотя бы отчасти пережили то, о чём рассказывают.\n  Поэтому лучше всего '
    'у киношников выходят фильмы про истеричных дегенератов, алкоголиков и проституток, а хуже всего - '
    'про добрых честных людей, хорошо делающих своё дело.',
    '   — Не знаю, пожуем - увидим! - сказал лев глядя на дрессировщика.',
    'Дальтоник Алексей до сих пор считает, что собирает Кубик Рубика за 14 секунд.',
]

# Оформление комплимента
FRAME_COMPLIMENTS = '\n🌟💫✨💫🌟💫✨💫🌟💫✨💫🌟\n'

# Список комплиментов
COMPLIMENTS = [
    'Ты — моя маленькая радость в большом мире.',
    'Ты делаешь мою жизнь лучше просто своим существованием.',
    'Ты как глоток свежего воздуха.',
    'Цвета кажутся ярче, когда ты рядом.',
    'Ты выявляешь лучшее в других людях.',
    'Ты как солнышко в дождливый день.',
    'Твоя улыбка заразительна.',
    'Ты — моя заветная любовь и воплощение самых лучших грез.',
    'Ты — лучик света в моей жизни.',
    'Твоя красивая улыбка — как солнечный луч в моем дне.',
    'Твоя интеллигентность и ум всегда меня вдохновляет.',
    'Твоя доброта и забота заставляют мир вокруг становиться добрее.',
    'Ты — источник вдохновения для меня. Твоя целеустремленность — впечатляющая.',
    'Ты делаешь мир ярче своим присутствием.',
    'С тобой, даже самый обычный день превращается в приключение, полное красок и эмоций.',
    'Твоя доброта и открытость создают вокруг атмосферу тепла и уюта. ',
    'Ты выглядишь так прекрасно, что я всегда теряюсь в поисках подходящих слов.',
    'Твое лицо — это шедевр искусства, созданный самой природой.',
    'Твоя улыбка способна оживить любое место и преобразить настроение окружающих.',
    'Твой талант и творческий потенциал безграничны. Ты умеешь превращать идеи в реальность.',
    'Твоя энергия и позитивное отношение к жизни притягивают всех вокруг. Ты создаешь атмосферу веселья и радости.',
    'Ты — источник вдохновения для всех вокруг. Твоя целеустремленность и умение добиваться своих целей восхищают.',
    'Твое умение поддерживать близких и быть рядом, когда им это нужно, делает тебя настоящим ангелом в жизни всех вокруг.',
    'Ты — невероятно талантливая и креативная личность. Твое творчество способно захватить сердца и умы.',
    'Ты обладаешь уникальной способностью видеть светлые стороны во всем.',
    'Твоя страсть к жизни и живое желание познавать мир заставляют всех вокруг видеть жизнь в новом свете.',
    'Твое умение находить баланс между умом и сердцем восхищает.',
    'Ты — цветок, который сияет даже в самый пасмурный день.',
    'С тобой время течет медленнее, и каждая секунда остается в памяти навечно.',
    'Твоя умелая рука способна превратить обычные вещи в произведения искусства.',
    'Ты как звезда, которая приносит свет в мою жизнь.',
    'Ты красивая песня, звучание которой затрагивает все струны моей души. С тобой я чувствую, что мир наполнен музыкой, и моё сердце слушает только твой ритм.',
    'В каждой твоей улыбке я вижу тысячу маленьких моментов счастья. Ты делаешь мою жизнь ярче, просто своим присутствием.',
    'Ты — мой источник вдохновения. Твоя сила преодолевать трудности, заставляет меня верить в чудеса.',
    'Твои слова озаряют мои дни, словно миллионы маленьких звезд, рассыпанных по небу ночью. Ты — мой мир, наполненный красотой и смыслом.',
    'Ты такой талантливый, что даже когда ошибаешься, это выглядит как произведение искусства.',
    'У тебя такие красивые глаза, что я забываю, о чем хотел поговорить.',
    'Если бы ум был валютой, у тебя была бы своя экономика!',
    'Ты так хорошо готовишь, что даже подгоревшая еда кажется шедевром.',
    'Ты умеешь слушать так, что даже молчание звучит как симфония.',
    'Ты излучаешь столько позитива, что солнечный свет завидует твоей энергии!',
]