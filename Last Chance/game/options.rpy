## Параметры игры "Будущее в моих руках"
## ===========================================

## Название и версия игры
define config.name = "Будущее в моих руках"
define config.version = "1.0"

## Имя папки для сохранений (в AppData на Windows)
define config.save_directory = "budushchee-1.0"

## Позволяет игроку менять настройки отображения (в окне / на весь экран)
define config.window = "auto"

## Переходы по умолчанию при смене экранов меню
define config.enter_transition = dissolve
define config.exit_transition = dissolve
define config.intra_transition = dissolve
define config.main_game_transition = dissolve
define config.game_main_transition = dissolve
define config.end_game_transition = fade

init python:
    if not hasattr(layout, 'yesno_prompt'):
        def retro_yesno_prompt(screen, message):
            # Передаем настоящие экшены Ren'Py вместо простых True/False
            return renpy.call_screen("custom_confirm", message=message, yes_action=Return(True), no_action=Return(False))
        layout.yesno_prompt = retro_yesno_prompt