## Определения персонажей и изображений
## =======================================

## --- ПЕРСОНАЖИ ---

define alex = Character(
    "Алекс",
    color="#7ab4ff",
    what_color="#ffffff",
    who_size=28,
    what_size=24
)

define masha = Character(
    "Маша",
    color="#ff8fab",
    what_color="#ffffff",
    who_size=28,
    what_size=24
)

define prof = Character(
    "Профессор Коваль",
    color="#c8a96e",
    what_color="#ffffff",
    who_size=28,
    what_size=24
)

define dima = Character(
    "Дима",
    color="#90c060",
    what_color="#ffffff",
    who_size=28,
    what_size=24
)

define katya = Character(
    "Катя",
    color="#c080e0",
    what_color="#ffffff",
    who_size=28,
    what_size=24
)

define narrator = Character(
    None,
    what_color="#e8e0d0",
    what_size=24
)

define thoughts = Character(
    "Алекс (мысли)",
    color="#7ab4ff",
    what_color="#c8e0ff",
    what_italic=True,
    who_size=24,
    what_size=22
)

## --- ИЗОБРАЖЕНИЯ: ФОНЫ ---

image bg university_hall = "images/bg/bg_university_hall.png"
image bg classroom = "images/bg/bg_classroom.png"
image bg dormitory = "images/bg/bg_dormitory.png"
image bg city_night = "images/bg/bg_city_night.png"
image bg cafe = "images/bg/bg_cafe.png"
image bg library = "images/bg/bg_library.png"
image bg roof = "images/bg/bg_roof.png"
image bg exam_hall = "images/bg/bg_exam_hall.png"
image bg park = "images/bg/bg_park.png"
image bg professors_office = "images/bg/bg_professors_office.png"
image bg future_city = "images/bg/bg_future_city.png"
image bg graduation = "images/bg/bg_graduation.png"

## --- ИЗОБРАЖЕНИЯ: ПЕРСОНАЖИ ---

## Алекс
image alex neutral = "images/characters/alex_neutral.png"
image alex happy = "images/characters/alex_happy.png"
image alex sad = "images/characters/alex_sad.png"
image alex surprised = "images/characters/alex_surprised.png"

## Маша
image masha neutral = "images/characters/masha_neutral.png"
image masha happy = "images/characters/masha_happy.png"
image masha sad = "images/characters/masha_sad.png"
image masha surprised = "images/characters/masha_surprised.png"

## Профессор Коваль
image prof neutral = "images/characters/prof_neutral.png"
image prof happy = "images/characters/prof_happy.png"
image prof angry = "images/characters/prof_angry.png"

## Дима
image dima neutral = "images/characters/dima_neutral.png"
image dima happy = "images/characters/dima_happy.png"
image dima sad = "images/characters/dima_sad.png"
image dima surprised = "images/characters/dima_surprised.png"

## Катя
image katya neutral = "images/characters/katya_neutral.png"
image katya happy = "images/characters/katya_happy.png"
image katya sad = "images/characters/katya_sad.png"
image katya surprised = "images/characters/katya_surprised.png"

## --- UI ---
image ui_title = "images/ui/title_bg.png"
image ui_textbox = "images/ui/textbox.png"

## --- ПЕРЕМЕННЫЕ ИГРЫ ---

default player_name = "Алекс"
default has_studied = False
default befriended_masha = False
default helped_prof = False
default impressed_dima = False
default romance_katya = False
default final_grade = 0
## Значения: "success", "mediocre", "failure", "secret"
default ending = ""
