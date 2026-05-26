## ================================================================
## "БУДУЩЕЕ В МОИХ РУКАХ"
## Визуальная новелла — Главный сценарий
## ================================================================

## ОБЪЯВЛЕНИЕ ПЕРСОНАЖЕЙ
define alex = Character("Алекс", color="#4a7acc")
define masha = Character("Маша", color="#ff9999")
define dima = Character("Дима", color="#66cc66")
define katya = Character("Катя", color="#ffcc66")
define prof = Character("Проф. Коваль", color="#cc3333")
define thoughts = Character("Мысли Алекса", kind=narrator, italic=True)

## ============================================================
## ЭКРАН ЗАСТАВКИ / TITLE
## ============================================================

label splashscreen:
    scene ui_title with dissolve
    pause 2.0
    return

## ============================================================
## НАЧАЛО ИГРЫ
## ============================================================

label start:
    # Принудительно включаем игровое меню при нажатии Esc
    $ _game_menu_screen = "game_menu"

    ## Музыка
    # play music "audio/music/ambient_morning.ogg" fadein 2.0

    ## --------------------------------------------------------
    ## СЦЕНА 01 — ОБЩЕЖИТИЕ, РАННЕЕ УТРО
    ## --------------------------------------------------------

    scene bg dormitory with fade
    pause 0.5

    narrator "Сентябрь. Первый год университета. Комната в общежитии пахнет свежей краской и чужими мечтами."

    show alex neutral at center
    with easeinbottom

    thoughts "Ну вот. Начинается."

    narrator "На экране монитора — расписание: сегодня первая лекция профессора Коваля по алгоритмам."

    narrator "Коваль — легенда факультета. Говорят, он режет студентов на экзамене без малейшего сожаления."

    thoughts "Пять лет. Пять лет — и у меня будет диплом. Или нет..."

    alex "Ладно. Главное — начать."

    hide alex with easeoutbottom
    pause 0.3

    ## --------------------------------------------------------
    ## СЦЕНА 02 — КОРИДОР УНИВЕРСИТЕТА
    ## --------------------------------------------------------

    scene bg university_hall with dissolve
    pause 0.3

    narrator "Коридор первого корпуса гудит от голосов. Первокурсники растеряно смотрят на расписание."

    show alex neutral at left
    with easeinbottom

    show masha happy at right
    with easeinbottom

    masha "Эй! Ты тоже на CS-101? Алгоритмы Коваля?"

    alex "Да... А ты давно здесь учишься? Не выглядишь потерянной."

    masha "Первый курс, как и ты! Просто я заранее скачала карту корпуса."

    masha "Маша. Группа 42-Б."

    alex "Алекс. Тоже 42-Б. Повезло."

    masha "Слышала, Коваль — монстр. Говорит только по делу, лишних баллов не даёт."

    show alex surprised at left

    alex "Отлично. Именно то, что мне было нужно в первый же день."

    show masha neutral at right

    masha "Не переживай! Говорят, если понять его логику — экзамен несложный. Главное — не пропускать."

    thoughts "Интересный человек. Кажется, у неё есть план."

    hide masha with easeoutbottom
    hide alex with easeoutbottom

    ## --------------------------------------------------------
    ## СЦЕНА 03 — АУДИТОРИЯ, ПЕРВАЯ ЛЕКЦИЯ
    ## --------------------------------------------------------

    scene bg classroom with dissolve
    pause 0.3

    # play music "audio/music/tense_lecture.ogg" fadein 1.5

    narrator "Аудитория 307. Профессор Коваль заходит ровно в 9:00 — секунда в секунду."

    show prof neutral at center
    with easeinbottom

    prof "Садитесь. Меня зовут Коваль Игорь Семёнович. Я не буду ни мотивировать вас, ни уговаривать учиться."

    prof "У вас есть один семестр. В конце — экзамен. Экзамен определит, останетесь ли вы на факультете."

    show alex neutral at left
    with easeinbottom

    show masha surprised at right
    with easeinbottom

    thoughts "Хорошее начало."

    prof "Задание первой недели: изучить три базовых алгоритма сортировки. Я проверю на практикуме в пятницу."

    prof "Кто не справится — получит первое предупреждение. Три предупреждения — отчисление."

    show masha sad at right

    masha "Это что, серьёзно?.."

    show prof angry at center

    prof "Вы хотите что-то сказать, студентка?"

    show masha neutral at right

    masha "Нет-нет, профессор. Всё ясно."

    show prof neutral at center

    prof "Прекрасно. Начнём."

    narrator "Два часа пролетели как один. В голове — сотни терминов. Руки устали записывать."

    hide prof with easeoutbottom
    hide masha with easeoutbottom
    hide alex with easeoutbottom

    ## --------------------------------------------------------
    ## СЦЕНА 04 — БИБЛИОТЕКА: ПЕРВАЯ РАЗВИЛКА
    ## --------------------------------------------------------

    scene bg library with dissolve
    pause 0.3

    # play music "audio/music/ambient_study.ogg" fadein 2.0

    narrator "После лекции Маша потащила Алекса в библиотеку."

    show alex neutral at left
    with easeinbottom

    show masha neutral at right
    with easeinbottom

    masha "Ну что, начнём готовиться к практикуму? У нас три дня."

    alex "Три дня — это звучит как много..."

    masha "Алекс, ты слышал Коваля? Три предупреждения — и до свидания!"

    show alex happy at left

    alex "Ладно, ладно. Ты права."

    narrator "На столе лежат учебники, ноутбук светится голубым экраном. За окном — солнечный сентябрьский день."

    thoughts "Выбор: провести вечер за учебниками... или сходить на вечеринку с соседями по общаге?"

    menu:
        "Остаться и серьёзно готовиться к практикуму":
            $ has_studied = True
            $ final_grade += 2

            show alex happy at left

            alex "Нет, давай останемся. Практикум важнее."

            show masha happy at right

            masha "Вот это правильный настрой! Давай разберём пузырьковую сортировку."

            narrator "Они просидели до закрытия библиотеки. К полуночи оба знали три алгоритма наизусть."

            thoughts "Может, это и есть начало чего-то большого?"

            $ befriended_masha = True

        "Пойти на вечеринку в общагру — один раз можно":
            $ has_studied = False

            show alex surprised at left

            alex "Слушай, там в общаге сейчас какой-то сбор первокурсников... Один вечер ничего не решит?"

            show masha sad at right

            masha "Алекс... ладно. Это твой выбор. Но я остаюсь."

            narrator "Вечеринка оказалась шумной, но пустой. Алекс вернулся в полночь с головной болью."

            thoughts "Может, зря. Маша, наверное, уже всё знает..."

    hide alex with easeoutbottom
    hide masha with easeoutbottom

    ## --------------------------------------------------------
    ## СЦЕНА 05 — КАФЕ: ЗНАКОМСТВО С ДИМОЙ И КАТЕЙ
    ## --------------------------------------------------------

    scene bg cafe with dissolve
    pause 0.3

    narrator "Среда. В студенческом кафе — шум, запах кофе и жареных пончиков."

    show alex neutral at left
    with easeinbottom

    show dima happy at right
    with easeinbottom

    dima "О, новенький! Ты же из группы Коваля? Слышал, как он вас встретил."

    alex "Уже разошлось по всему факультету?"

    show dima neutral at right

    dima "Дима. Второй курс. Прошлый год выжил — и ты выживешь."

    show katya happy at center
    with easeinbottom

    katya "Привет! Я Катя. Тоже второй курс. Не слушай Диму — он преувеличивает."

    alex "Рад познакомиться. Вы как... вообще справляетесь?"

    dima "Секрет? Не пытайся угодить Ковалю. Просто реши его задачи лучше всех в группе."

    show katya neutral at center

    katya "Или... найди то, что тебя действительно зажигает. У меня это стартапы. Я совмещаю учёбу с работой в акселераторе."

    show alex surprised at left

    alex "Акселератор? Серьёзно? Как ты успеваешь?"

    katya "Приоритеты. И очень мало сна."

    show dima happy at right

    dima "Кстати, в эту пятницу хакатон. Вузовский. Три человека в команде, 24 часа, задача по ML."

    dima "Нам нужен третий. Ты как?"

    thoughts "Хакатон... Это не учёба. Но это опыт. И связи."

    menu:
        "Согласиться — хакатон даст реальный опыт":
            $ impressed_dima = True
            $ final_grade += 1

            alex "Я в деле. Что нужно уметь?"

            show dima happy at right

            dima "Отлично! Python знаешь?"

            alex "На базовом уровне."

            show katya happy at center

            katya "Хватит. Остальное — по ходу."

            narrator "Алекс записал номера Димы и Кати. Перед ним открывался новый мир — мир людей, которые уже делают."

        "Отказаться — лучше сфокусироваться на Ковале":
            alex "Спасибо, но... сейчас не время. Коваль и так жмёт."

            show dima neutral at right

            dima "Понимаю. Если передумаешь — пиши."

            thoughts "Правильное решение? Или я просто боюсь рисковать?"

    hide alex with easeoutbottom
    hide dima with easeoutbottom
    hide katya with easeoutbottom

    ## --------------------------------------------------------
    ## СЦЕНА 06 — НОЧНОЙ ГОРОД: ВЫБОР ПУТИ
    ## --------------------------------------------------------

    scene bg city_night with dissolve
    pause 0.5

    # play music "audio/music/city_night_ambient.ogg" fadein 2.0

    narrator "Пятница. Город горит огнями. Алекс стоит у окна общежития и думает."

    show alex neutral at center
    with easeinbottom

    thoughts "Прошли две недели. Я узнал многое. Но чего я хочу на самом деле?"

    narrator "На телефоне — три непрочитанных сообщения:"
    narrator "Маша: «Коваль объявил дополнительный проект. Хочешь объединиться?»"
    narrator "Дима: «Хакатон закончили. Заняли второе место. Следующий — через месяц.»"
    narrator "Незнакомый номер: «Стажировка в IT-компании. Рекомендовал профессор Коваль.»"

    show alex surprised at center

    thoughts "Коваль... рекомендовал меня? Но мы почти не общались."

    narrator "Три дороги. Три выбора. Они не исключают друг друга — но времени на всё не хватит."

    menu:
        "Написать Маше — сделать проект вместе":
            $ befriended_masha = True
            $ final_grade += 2

            alex "Маша — надёжный человек. Проект — это оценка."

            thoughts "Учёба прежде всего. Я же пришёл за дипломом."

            jump scene07_office

        "Написать Диме — участвовать в следующем хакатоне":
            $ impressed_dima = True
            $ final_grade += 1

            alex "Хакатон — это реальные навыки. Рынку нужен опыт, а не оценки."

            thoughts "Буду строить портфолио. Диплом не кормит — проекты кормят."

            jump scene07_office

        "Позвонить по поводу стажировки":
            $ helped_prof = True
            $ final_grade += 3

            alex "Стажировка. Коваль что-то знает, что я пока не понимаю."

            thoughts "Если уж сам профессор рекомендовал — надо разобраться."

            jump scene07_office

## --------------------------------------------------------
## СЦЕНА 07 — КАБИНЕТ ПРОФЕССОРА
## --------------------------------------------------------

label scene07_office:

    hide alex with easeoutbottom
    scene bg professors_office with dissolve
    pause 0.3

    # play music "audio/music/tense_ambient.ogg" fadein 1.5

    narrator "Понедельник. Алекс стоит перед дверью кабинета профессора Коваля."

    narrator "Табличка: «Коваль И.С. — приём по средам с 14:00»."

    thoughts "Не среда. Но дверь открыта."

    show prof neutral at center
    with easeinbottom

    show alex neutral at left
    with easeinbottom

    prof "А, студент. Заходите."

    alex "Добрый день, профессор. Я пришёл по поводу стажировки... или проекта. Честно говоря, я ещё не до конца определился."

    show prof happy at center

    prof "Наконец-то честный ответ. Большинство делают вид, что у них всё под контролем."

    prof "Садитесь. Расскажите — что вас интересует в алгоритмах? Не для оценки — для себя."

    thoughts "Серьёзный вопрос."

    show alex happy at left

    ## ИСПРАВЛЕНЫ ОТСТУПЫ СТРОК ДИАЛОГОВ ВНУТРИ IF/ELSE
    if has_studied:
        alex "Меня интересует оптимизация. Когда алгоритм элегантен — это почти красота."
        prof "Хм. Это... неожиданно зрелый ответ для первокурсника."
        $ helped_prof = True
        $ final_grade += 2
    else:
        alex "Честно? Я ещё не знаю. Но что-то в этом есть. Что-то... важное."
        prof "Неплохой ответ. Неуверенность — не слабость, если за ней стоит желание найти."
        $ final_grade += 1

    prof "Я дам вам задачу. Не обязательную. Если решите — будут возможности."

    prof "Если не решите — ничего страшного. Но я посмотрю, как вы думаете."

    show alex surprised at left

    alex "Что за задача?"

    prof "Напишите эссе: «В чём разница между умным студентом и успешным человеком?» Две страницы. К следующей неделе."

    show prof neutral at center

    prof "Это не задание по алгоритмам. Это задание по жизни."

    hide prof with easeoutbottom
    hide alex with easeoutbottom

    jump scene08_roof

## --------------------------------------------------------
## СЦЕНА 08 — КРЫША: КАТЯ И РАЗГОВОР О БУДУЩЕМ
## --------------------------------------------------------

label scene08_roof:

    scene bg roof with dissolve
    pause 0.5

    # play music "audio/music/rooftop_evening.ogg" fadein 2.0

    narrator "Вечер. Алекс поднялся на крышу общежития — подумать."

    show alex neutral at right
    with easeinbottom

    narrator "Там уже кто-то был."

    show katya neutral at left
    with easeinbottom

    katya "О! Ты тоже сюда приходишь думать?"

    alex "Похоже, мы оба ищем тишину в шумном месте."

    katya "Красиво звучит. Можно украду для презентации?"

    show alex happy at right

    alex "Бери. Как хакатон с Димой?"

    show katya happy at left

    katya "Второе место — неплохо для новой команды. Но первое возьмём в следующий раз."

    katya "А ты как? Слышала, Коваль тебя выделил на лекции."

    alex "Выделил? Или отругал?"

    show katya neutral at left

    katya "Выделил. Он сказал, что ты правильно поставил вопрос. Для Коваля это высшая похвала."

    thoughts "Интересно."

    show alex neutral at right

    alex "Катя... ты уже знаешь, кем хочешь быть?"

    katya "В смысле — профессии?"

    alex "В смысле — вообще. Через пять лет. Через десять."

    show katya sad at left

    katya "Знаешь... иногда мне страшно. Что я работаю-работаю, строю-строю... а зачем? Для кого?"

    show alex neutral at right

    alex "Может, для себя?"

    show katya happy at left

    katya "Слишком просто."

    alex "Или именно так и должно быть."

    narrator "Они сидели на крыше ещё час. Говорили о будущем — и оно казалось чуть ближе."

    menu:
        "Спросить номер телефона Кати":
            alex "Катя... хотел бы продолжить этот разговор. Как-нибудь ещё раз."
            show katya happy at left
            katya "Мне тоже. Пиши."
            $ romance_katya = True

        "Просто попрощаться":
            alex "Спасибо за разговор. Мне нужно подумать над эссе Коваля."
            show katya neutral at left
            katya "Эссе? Он дал тебе задание? Это значит — он видит в тебе потенциал."

    hide katya with easeoutbottom
    hide alex with easeoutbottom

    jump scene09_park

## --------------------------------------------------------
## СЦЕНА 09 — ПАРК: МАША С НОВОСТЯМИ
## --------------------------------------------------------

label scene09_park:

    scene bg park with dissolve
    pause 0.3

    # play music "audio/music/ambient_park.ogg" fadein 2.0

    narrator "За неделю до экзамена. Маша позвонила — попросила встретиться в парке."

    show masha sad at left
    with easeinbottom

    show alex neutral at right
    with easeinbottom

    alex "Маша, что случилось? Ты в сообщении написала «срочно»."

    masha "Алекс... у меня проблемы. Я провалила промежуточный тест. Если провалю экзамен — меня отчислят."

    show alex surprised at right

    alex "Что? Но ты же... ты лучше всех нас разбирается в материале!"

    show masha sad at left

    masha "Я разбираюсь в теории. Но на тесте был практический блок. Я растерялась. Не успела."

    masha "И ещё... дома проблемы. Мама заболела. Мне нужно помогать, а я здесь..."

    thoughts "Вот оно. Реальная жизнь — она не спрашивает разрешения."

    menu:
        "Предложить помочь с подготовкой к экзамену":
            $ befriended_masha = True
            $ final_grade += 1

            alex "Маша, слушай. У нас ещё неделя. Давай каждый вечер — я, ты, библиотека."

            show masha surprised at left

            masha "Но у тебя же своя подготовка..."

            show alex happy at right

            alex "Объяснять — лучший способ выучить самому. Ты мне поможешь не меньше, чем я тебе."

            show masha happy at left

            masha "Алекс... спасибо. Правда."

        "Посоветовать поговорить с деканом":
            alex "Маша, ты слышала о льготном экзамене? Если есть семейные обстоятельства — декан может помочь."

            show masha surprised at left

            masha "Я... не думала об этом. Думала, что просто нужно справиться."

            alex "Справиться — можно по-разному. Иногда просить о помощи — тоже сила."

            show masha neutral at left

            masha "Может, ты и прав."

        "Сказать, что у тебя нет времени":
            show alex sad at right

            alex "Маша, я... понимаю. Но у меня самого критичная неделя. Я не могу..."

            show masha sad at left

            masha "Нет, я понимаю. Прости, что загрузила тебя."

            thoughts "Может, я ошибся?"

    hide masha with easeoutbottom
    hide alex with easeoutbottom

    jump scene10_exam

## --------------------------------------------------------
## СЦЕНА 10 — ЭКЗАМЕН (КУЛЬМИНАЦИЯ)
## --------------------------------------------------------

label scene10_exam:

    scene bg exam_hall with dissolve
    pause 0.5

    # play music "audio/music/tense_exam.ogg" fadein 1.0

    narrator "День X. Экзамен по алгоритмам профессора Коваля."

    narrator "Зал тихий. Слышно только скрип ручек и дыхание восьмидесяти студентов."

    show alex neutral at center
    with easeinbottom

    thoughts "Вот оно. Всё, что было — учёба, разговоры, ночи над конспектами — всё ради этого."

    show prof neutral at left
    with easeinbottom

    prof "Время пошло. У вас два часа. Удачи."

    narrator "Алекс смотрит на лист. Первый вопрос — сортировка. Второй — граф. Третий — динамическое программирование."

    ## ИСПРАВЛЕНЫ ОТСТУПЫ ДИАЛОГОВ ВНУТРИ IF/ELSE
    if has_studied:
        thoughts "Я это знаю. Я это учил. Пузырьковая... нет, здесь быстрее будет merge sort."
        narrator "Пальцы уверенно движутся. Ответы выстраиваются сами."
        $ final_grade += 3
    else:
        thoughts "Я... помню это. Кажется. Маша что-то объясняла про графы..."
        narrator "Алекс напрягает память. Не всё выходит легко — но логика выручает."
        $ final_grade += 1

    if befriended_masha:
        narrator "В середине зала — Маша. Видно, что ей нелегко. Но она держится."

    narrator "Последний вопрос: «Опишите ситуацию, когда эффективность алгоритма важнее его правильности.»"

    thoughts "Это... это не про алгоритмы. Это про жизнь."

    ## ИСПРАВЛЕНЫ ОТСТУПЫ ДИАЛОГОВ ВНУТРИ IF/ELSE
    if helped_prof:
        thoughts "Эссе. «Умный студент знает правильный ответ. Успешный человек знает, какой ответ нужен сейчас.»"
        narrator "Алекс пишет уверенно — полторы страницы за десять минут."
        $ final_grade += 2
    else:
        thoughts "Реальный мир не всегда ждёт идеального решения."
        narrator "Алекс пишет честно, из опыта последних недель."
        $ final_grade += 1

    narrator "Два часа. Время вышло."

    prof "Ручки на стол."

    hide prof with easeoutbottom
    hide alex with easeoutbottom

    scene bg professors_office with dissolve

    narrator "Через три дня — результаты."

    show prof neutral at center
    with easeinbottom

    show alex neutral at left
    with easeinbottom

    # Распределение концовок по баллам
    if final_grade >= 11:
        prof "Студент... я редко говорю это. Но ваша работа — лучшая на потоке."
        $ ending = "success"
        jump scene11_future_success
    elif final_grade >= 7:
        prof "Хорошо. Не блестяще — но честно. Вы думаете. Продолжайте."
        $ ending = "mediocre"
        jump scene11_future_mediocre
    elif final_grade >= 4:
        prof "Вы сдали. Едва. Но сдали."
        $ ending = "failure"
        jump scene11_future_struggle
    else:
        prof "Студент... вам нужно серьёзно пересмотреть приоритеты."
        $ ending = "secret" # Перенаправляем на 4-ю скрытую концовку
        jump scene11_future_struggle

## --------------------------------------------------------
## СЦЕНА 11А — ВИДЕНИЕ БУДУЩЕГО (УСПЕХ)
## --------------------------------------------------------

label scene11_future_success:

    hide prof with easeoutbottom
    hide alex with easeoutbottom

    scene bg future_city with dissolve
    pause 1.0

    # play music "audio/music/triumphant_ambient.ogg" fadein 2.0

    narrator "..."

    narrator "Алекс закрывает глаза — и видит."

    show alex happy at center
    with dissolve

    thoughts "Это... будущее?"

    narrator "Огни города — не просто огни. Это алгоритмы, пульсирующие в сетях. Это данные, текущие рекой."

    thoughts "Я написал часть этого. Маленькую часть. Но мою."

    narrator "Стажировка переросла в должность. Проекты с Димой стали стартапом. Катя..."

    if romance_katya:
        thoughts "Катя всё ещё рядом. И она права — мы строим это для себя. И друг для друга."
    else:
        thoughts "Катя запустила свой стартап. Иногда мы пересекаемся на конференциях."

    if befriended_masha:
        thoughts "Маша сдала экзамен. Теперь она ведёт собственный курс по алгоритмам."

    narrator "Будущее — не место назначения. Это то, что ты строишь каждый день."

    hide alex with dissolve

    jump scene12_ending

## --------------------------------------------------------
## СЦЕНА 11Б — ВИДЕНИЕ БУДУЩЕГО (СРЕДНИЙ РЕЗУЛЬТАТ)
## --------------------------------------------------------

label scene11_future_mediocre:

    hide prof with easeoutbottom
    hide alex with easeoutbottom

    scene bg future_city with dissolve
    pause 1.0

    narrator "..."

    narrator "Алекс смотрит на огни города. Думает."

    show alex neutral at center
    with dissolve

    thoughts "Я не был лучшим. Но я был честным."

    narrator "Второй курс оказался тяжелее первого. Третий — ещё тяжелее."

    narrator "Но каждый раз — чуть лучше. Чуть увереннее."

    thoughts "Может, это и есть путь? Не взлететь сразу — а идти?"

    narrator "Через пять лет Алекс получил диплом. Не с отличием — но с честью."

    narrator "И это тоже — будущее в руках."

    hide alex with dissolve

    jump scene12_ending

## --------------------------------------------------------
## СЦЕНА 11В — ВИДЕНИЕ БУДУЩЕГО (ТРУДНЫЙ ПУТЬ)
## --------------------------------------------------------

label scene11_future_struggle:

    hide prof with easeoutbottom
    hide alex with easeoutbottom

    scene bg city_night with dissolve
    pause 1.0

    narrator "Ночь. Город не спит — и Алекс не спит."

    show alex sad at center
    with dissolve

    thoughts "Я не справился так, как хотел. Это больно."

    narrator "Но боль — не конец. Это урок."

    thoughts "Что я делал не так? Слишком много распылялся? Слишком мало фокусировался?"

    narrator "Алекс открывает ноутбук. Начинает сначала — более осознанно."

    show alex neutral at center

    if ending == "secret":
        thoughts "Мне нужен свой собственный путь. Иначе я просто потеряю себя."
    else:
        thoughts "Будущее — оно всё ещё моё. Просто путь к нему чуть длиннее, чем я думал."

    narrator "Иногда самый важный успех — это встать после падения."

    hide alex with dissolve

    jump scene12_ending

## --------------------------------------------------------
## СЦЕНА 12 — ФИНАЛ И КОНЦОВКИ
## --------------------------------------------------------

label scene12_ending:

    scene bg graduation with dissolve
    pause 0.5

    # play music "audio/music/ending_theme.ogg" fadein 2.0

    narrator "..."

    if ending == "success":
        ## КОНЦОВКА 1 — ТРИУМФ
        narrator "Церемония вручения дипломов. Имя Алекса звучит первым в списке отличников."

        show alex happy at center
        with easeinbottom

        if befriended_masha:
            show masha happy at left
            with easeinbottom
            masha "Мы сделали это, Алекс! Вместе!"

        if romance_katya:
            show katya happy at right
            with easeinbottom
            katya "Ты ведь знал, что так будет, да?"

        show alex happy at center

        alex "Честно? Нет. Но я верил, что стоит попробовать."

        narrator "Профессор Коваль смотрит из первого ряда. Что-то похожее на улыбку."

        thoughts "Будущее — в моих руках. Я сделал его сам."

        narrator "{b}КОНЕЦ — «Восхождение»{/b}"
        narrator "{i}Лучший возможный исход. Ты нашёл баланс между учёбой, дружбой и ростом.{/i}"

    elif ending == "mediocre":
        ## КОНЦОВКА 2 — ЧЕСТНЫЙ ПУТЬ
        narrator "Церемония вручения дипломов. Алекс — в середине списка. Как большинство."

        show alex neutral at center
        with easeinbottom

        if befriended_masha:
            show masha neutral at left
            with easeinbottom
            masha "Мы справились. Может, не на отлично — но справились."

        alex "Знаешь, Маша... Я думал, что «успех» — это быть первым. Теперь не уверен."

        if befriended_masha:
            masha "Может, успех — это просто не сдаваться?"

        thoughts "Я не гений. Но я — настойчивый. И это тоже что-то значит."

        narrator "{b}КОНЕЦ — «Твёрдый шаг»{/b}"
        narrator "{i}Ты выжил. Ты вырос. Путь продолжается.{/i}"

    elif ending == "failure":
        ## КОНЦОВКА 3 — ВТОРОЙ ШАНС
        narrator "Алекс не на церемонии. Он в библиотеке — готовится к пересдаче."

        show alex sad at center
        with easeinbottom

        thoughts "Я мог бы злиться. На Коваля, на систему, на обстоятельства."

        thoughts "Но если честно — я сам сделал эти выборы."

        show alex neutral at center

        alex "Ладно. Второй шанс — это тоже шанс."

        narrator "Пересдача. Алекс сдаёт — лучше, чем в первый раз."

        narrator "Потому что теперь он знает: будущее строится не за один экзамен."

        narrator "{b}КОНЕЦ — «Второй шанс»{/b}"
        narrator "{i}Падения — часть пути. Важно встать.{/i}"

    else:
        ## КОНЦОВКА 4 — ТАЙНЫЙ ПУТЬ
        narrator "Иногда история не идёт по плану."

        show alex neutral at center
        with easeinbottom

        thoughts "Я не стал отличником. Не стал предпринимателем."

        thoughts "Я стал... собой. И это оказалось сложнее всего."

        narrator "Алекс взял академический отпуск. Уехал. Поработал. Вернулся."

        show alex happy at center

        thoughts "Теперь я знаю, зачем учусь. И это меняет всё."

        narrator "{b}КОНЕЦ — «Свой путь»{/b}"
        narrator "{i}Нет единственно правильной дороги к будущему.{/i}"

    ## ФИНАЛЬНОЕ СЛОВО
    pause 0.5

    if romance_katya:
        hide katya with dissolve
    if befriended_masha:
        hide masha with dissolve
    hide alex with dissolve

    scene ui_title with dissolve

    narrator " "

    narrator "{b}«Будущее в моих руках»{/b}"
    narrator " "
    narrator "Каждый выбор — кирпич в фундаменте твоей жизни."
    narrator "Учись не ради оценок, а ради понимания."
    narrator "Дружи не ради пользы, а ради роста."
    narrator "И помни: успех — это не пункт назначения."
    narrator " "
    narrator "{i}Это то, кем ты становишься по дороге.{/i}"

    pause 1.0

    narrator " "
    narrator "{size=18}— Конец —{/size}"

    pause 2.0

    return