## Экраны интерфейса для "Будущее в моих руках"
## =================================================

## -------------------------------------------------------
## ЭКРАН ДИАЛОГА
## -------------------------------------------------------

screen say(who, what):
    style_prefix "say"

    window:
        id "window"
        background Frame("images/ui/textbox.png", 20, 10)
        xfill True
        ysize 185
        yalign 1.0
        yoffset -10

        if who is not None:
            window:
                id "namebox"
                style "namebox"
                text who id "who"

        text what id "what"

style window is default
style say_window is window
style namebox is default
style say_dialogue is default
style say_thought is say_dialogue

style say_window:
    xalign 0.5
    xfill True
    yalign 1.0
    ysize 185

style namebox:
    xpos 220
    xanchor 0.0
    xsize 300
    ypos -28
    ypadding 5
    background Frame("#1a1440cc", 5, 5)
    padding (15, 5)

style say_dialogue:
    xpos 226
    xanchor 0.0
    xsize 936
    ypos 60
    color "#f0ece0"  # ИСПРАВЛЕНО: Было text_color
    size 24         # ИСПРАВЛЕНО: Было text_size
    line_spacing 5

## -------------------------------------------------------
## ЭКРАН ВЫБОРА
## -------------------------------------------------------

screen choice(items):
    style_prefix "choice"

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 10

        for i in items:
            textbutton i.caption:
                action i.action
                background Frame("#0f0820cc", 15, 10)
                hover_background Frame("#2a3a8acc", 15, 10)
                xsize 900
                xalign 0.5
                padding (30, 15)
                text_xalign 0.5
                text_color "#cccccc"
                text_hover_color "#ffffff"
                text_size 22

## -------------------------------------------------------
## ГЛАВНОЕ МЕНЮ
## -------------------------------------------------------

screen main_menu():
    tag menu
    style_prefix "main_menu"

    add "images/ui/title_bg.png"

    ## Затемнение для читаемости
    add Solid("#00000060")

    vbox:
        xalign 0.5
        yalign 0.35
        spacing 5

        ## Название игры
        text "БУДУЩЕЕ В МОИХ РУКАХ":
            xalign 0.5
            color "#e8d870"
            size 52
            bold True
            outlines [(2, "#000000", 0, 0)]

        text "визуальная новелла":
            xalign 0.5
            color "#8899cc"
            size 20
            italic True

    vbox:
        xalign 0.5
        yalign 0.65
        spacing 18

        textbutton "Начать игру":
            xalign 0.5
            xsize 320
            action Start()
            background Frame("#1a1440cc", 10, 8)
            hover_background Frame("#2a3a8acc", 10, 8)
            padding (30, 12)
            text_xalign 0.5
            text_color "#ffffff"
            text_hover_color "#e8d870"
            text_size 24

        textbutton "Загрузить":
            xalign 0.5
            xsize 320
            action ShowMenu("load")
            background Frame("#1a1440cc", 10, 8)
            hover_background Frame("#2a3a8acc", 10, 8)
            padding (30, 12)
            text_xalign 0.5
            text_color "#cccccc"
            text_hover_color "#e8d870"
            text_size 24

        textbutton "Настройки":
            xalign 0.5
            xsize 320
            action ShowMenu("preferences")
            background Frame("#1a1440cc", 10, 8)
            hover_background Frame("#2a3a8acc", 10, 8)
            padding (30, 12)
            text_xalign 0.5
            text_color "#cccccc"
            text_hover_color "#e8d870"
            text_size 24

        textbutton "Выход":
            xalign 0.5
            xsize 320
            action Quit(confirm=False)
            background Frame("#1a1440cc", 10, 8)
            hover_background Frame("#44113acc", 10, 8)
            padding (30, 12)
            text_xalign 0.5
            text_color "#cccccc"
            text_hover_color "#ff8888"
            text_size 24

    ## Версия
    text "v1.0 — Учебный проект":
        xalign 1.0
        yalign 1.0
        xoffset -20
        yoffset -10
        color "#44556688"
        size 16

## -------------------------------------------------------
## МЕНЮ ПАУЗЫ (GAME MENU)
## -------------------------------------------------------

screen game_menu(title=_("Меню"), scroll=None, yinitial=0.0):
    style_prefix "game_menu"

    if main_menu:
        add ui._window_color()
    else:
        add "images/ui/title_bg.png"
        add Solid("#00000088")

    frame:
        style "game_menu_outer_frame"

        hbox:
            frame:
                style "game_menu_navigation_frame"
                vbox:
                    style "game_menu_nav_vbox"

                    textbutton "История":
                        action ShowMenu("history")
                    textbutton "Сохранить":
                        action ShowMenu("save")
                    textbutton "Загрузить":
                        action ShowMenu("load")
                    textbutton "Настройки":
                        action ShowMenu("preferences")
                    textbutton "Главное меню":
                        action MainMenu()
                    textbutton "Выход":
                        action Quit(confirm=False)

            frame:
                style "game_menu_content_frame"

                if scroll == "viewport":
                    viewport:
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                elif scroll == "vpgrid":
                    vpgrid:
                        cols 1
                        yinitial yinitial
                        scrollbars "vertical"
                        mousewheel True
                        draggable True
                        pagekeys True
                        side_yfill True
                        transclude
                else:
                    transclude

    use navigation

    label title xpos 40 ypos 20:
        style "game_menu_label"
        text_style "game_menu_label_text"

style game_menu_outer_frame is empty
style game_menu_navigation_frame is empty
style game_menu_content_frame is empty
style game_menu_label is default
style game_menu_label_text is default

style game_menu_outer_frame:
    bottom_margin 45

style game_menu_navigation_frame:
    xsize 280
    yfill True

style game_menu_content_frame:
    left_margin 40
    right_margin 20
    top_margin 10

style game_menu_label:
    xpos 75
    ysize 120

style game_menu_label_text:
    size 38
    color "#e8d870"
    yalign 0.5
    bold True

style game_menu_nav_vbox:
    xpos 60
    xanchor 1.0
    xsize 280
    yalign 0.5
    spacing 8

## -------------------------------------------------------
## НАВИГАЦИЯ (НПК в меню)
## -------------------------------------------------------

screen navigation():
    vbox:
        style_prefix "navigation"
        
        xpos 40          # Сдвигаем меню вправо от края экрана, чтобы текст не резался
        yalign 0.5       # Центрируем по вертикали
        spacing 15       # Расстояние между кнопками

        textbutton _("Вернуться") action Return()
        textbutton _("Сохранить") action ShowMenu("save")
        textbutton _("Загрузить") action ShowMenu("load")
        textbutton _("Настройки") action ShowMenu("preferences")
        textbutton _("Главное меню") action MainMenu()
        textbutton _("Выход") action Quit()

style navigation_button is gui_button
style navigation_button_text is gui_button_text

style navigation_button:
    size_group "navigation"
    properties gui.button_properties("navigation_button")
    background None  # <-- ДОБАВЬ ЭТУ СТРОЧКУ

style navigation_button_text:
    properties gui.button_text_properties("navigation_button")

## -------------------------------------------------------
## ЭКРАН ИСТОРИИ ДИАЛОГОВ
## -------------------------------------------------------

screen history():
    tag menu

    predict False
    use game_menu("История", scroll=("vpgrid" if gui.history_height else "viewport"), yinitial=1.0):

        style_prefix "history"

        for h in renpy.history.history:
            window:
                has hbox

                # ИСПРАВЛЕНО: Конструкция заменена на валидный Screen Language блок
                if h.who:
                    label h.who:
                        xsize 150
                else:
                    label "":
                        xsize 150

                text h.what:
                    xsize 700

define gui.history_height = 210
define gui.history_max = 250

## -------------------------------------------------------
## БЫСТРЫЕ МЕНЮ (внутри диалога)
## -------------------------------------------------------

screen quick_menu():
    zorder 100
    style_prefix "quick"

    if quick_menu:
        hbox:
            style_prefix "quick"
            xalign 0.5
            yalign 1.0
            yoffset -195

            textbutton "Назад" action Rollback()
            textbutton "Авто" action Preference("auto-forward", "toggle")
            textbutton "Пропустить" action Skip() alternate Skip(fast=True, confirm=True)
            textbutton "Лог" action ShowMenu("history")
            textbutton "Сохранить" action ShowMenu("save")
            textbutton "Настройки" action ShowMenu("preferences")
            textbutton "Скрыть" action HideInterface()

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")
    size 18
    color "#8899cc"
    hover_color "#aabbee"

default quick_menu = True

## -------------------------------------------------------
## ЭКРАНЫ СОХРАНЕНИЯ И ЗАГРУЗКИ
## -------------------------------------------------------

screen save():
    tag menu
    use file_slots(_("Сохранить"))

screen load():
    tag menu
    use file_slots(_("Загрузить"))

screen file_slots(title):

    default page = "1"

    use game_menu(title):

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 20

            # Переключатели страниц
            hbox:
                xalign 0.5
                spacing 10
                
                textbutton _("<") action FilePagePrevious()
                textbutton _("1") action FilePage(1)
                textbutton _("2") action FilePage(2)
                textbutton _("3") action FilePage(3)
                textbutton _("4") action FilePage(4)
                textbutton _(">") action FilePageNext()

            # Сетка слотов 3x2
            grid 3 2:
                xalign 0.5
                spacing 15
                style_prefix "slot"

                for i in range(1, 7):
                    button:
                        # Теперь игра смотрит на то, КАКОЙ заголовок у экрана ("Сохранить" или "Загрузить")
                        if title == _("Загрузить"):
                            action FileLoad(i, confirm=True)
                        else:
                            action FileSave(i, confirm=True)
                            
                        xsize 220
                        ysize 160
                        background "#1a1a1a"
                        hover_background "#333333"

                        vbox:
                            xalign 0.5
                            yalign 0.5
                            spacing 10

                            add FileScreenshot(i) xalign 0.5 yalign 0.5

                            text FileTime(i, empty=_("Пустой слот")):
                                style "slot_button_text"
                                size 14
                                xalign 0.5
style slot_button_text is text

# Создаем свой собственный экран подтверждения с нуля
screen custom_confirm(message, yes_action, no_action):
    modal True # Блокирует клики по нижним слоям игры, пока открыто окно

    # Фон затемнения
    add "#000000b3" 

    # Центрированное диалоговое окошко
    frame:
        background "#1a1a1a"
        xalign 0.5
        yalign 0.5
        xpadding 40
        ypadding 30
        
        vbox:
            xalign 0.5
            spacing 30

            # Текст вопроса (например: "Вы хотите перезаписать это сохранение?")
            text message:
                color "#ffffff"
                size 20
                xalign 0.5
                justify True

            # Кнопки "Да" и "Нет"
            hbox:
                xalign 0.5
                spacing 50

                textbutton _("Да"):
                    action yes_action
                    text_size 22
                    text_hover_color "#ffcc66" # Подсвечивается при наведении

                textbutton _("Нет"):
                    action no_action
                    text_size 22
                    text_hover_color "#ffcc66"