## GUI настройки для "Будущее в моих руках"
## ==========================================

## Шрифты (используем системные)
define gui.default_font = "DejaVuSans.ttf"
define gui.name_font = "DejaVuSans-Bold.ttf"
define gui.interface_font = "DejaVuSans.ttf"

## Основные настройки интерфейса

## Окно диалога
define gui.textbox_height = 185
define gui.textbox_yalign = 1.0

## Имя персонажа
define gui.name_xpos = 226
define gui.name_ypos = 0
define gui.name_xalign = 0.0
define gui.name_yalign = 0.0
define gui.name_text_size = 28

## Диалоговый текст
define gui.dialogue_xpos = 226
define gui.dialogue_ypos = 60
define gui.dialogue_text_size = 24
define gui.dialogue_width = 936

## Размеры спрайтов
define gui.sprite_xpos = 0.5
define gui.sprite_ypos = 1.0

## Меню выбора
define gui.choice_button_width = 790
define gui.choice_button_height = None
define gui.choice_button_tile = False

## Цвета меню выбора
define gui.choice_button_text_idle_color = '#cccccc'
define gui.choice_button_text_hover_color = '#ffffff'
define gui.choice_button_text_insensitive_color = '#555555'

## Кнопки
define gui.button_text_font = gui.interface_font
define gui.button_text_size = 24

## Базовые свойства кнопок (ИСПРАВЛЕНО ДЛЯ НАВИГАЦИИ)
define gui.button_width = None
define gui.button_height = None
define gui.button_tile = False
define gui.button_borders = Borders(5, 5, 5, 5)

define gui.navigation_button_width = None
define gui.navigation_button_borders = Borders(5, 5, 5, 5)
define gui.navigation_button_tile = False

define gui.quick_button_borders = Borders(5, 5, 5, 5)
define gui.quick_button_tile = False

## Прокрутка
define gui.scrollbar_size = 12
define gui.slider_size = 30

## Основной цвет акцента (синий, как учёба)
define gui.accent_color = '#4a7acc'
define gui.selected_color = '#ffffff'
define gui.idle_color = '#aaaaaa'
define gui.hover_color = '#ffffff'
define gui.insensitive_color = '#5555557f'

define gui.muted_color = '#336699'
define gui.hover_muted_color = '#6699cc'

## Текстовый ящик
define gui.textbox_color = None

## Шрифт основного текста
define gui.text_font = "DejaVuSans.ttf"
define gui.text_size = 24
define gui.text_color = '#f0ece0'

## Цвет фона диалога
define gui.textbox_unscrolled_color = '#00000080'

## Оверлей
define config.overlay_functions = []

## Позиции персонажей на экране
define left = Position(xalign=0.15, yalign=1.0)
define right = Position(xalign=0.85, yalign=1.0)
define center = Position(xalign=0.5, yalign=1.0)
define offscreen_left = Position(xalign=-0.1, yalign=1.0)
define offscreen_right = Position(xalign=1.1, yalign=1.0)