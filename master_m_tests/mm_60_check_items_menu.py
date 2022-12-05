import time

import pyautogui
from pywinauto_recorder.player import *

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Загрузить карту||Button")

with Window(u"Загрузка карты||Window"):
    left_click(u"||TitleBar")
    left_click(u" Вниз||ComboBox")
    for _ in range(50):
        send_keys('{DOWN down}')
    send_keys('{DOWN up}')
    send_keys('{ENTER}')
    send_keys('{ENTER}')
    time.sleep(15)

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->||Pane->||Custom"):
        left_click(u"||Custom#[0,0]")
        time.sleep(1)
        pyautogui.doubleClick()
        time.sleep(2)

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        right_click(u"МД1-1РУ+4С||TreeItem")

with Window(u"||Menu"):
    move(u"Обновить (F5)||MenuItem")
    left_click(u"Свойства||MenuItem")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window-> МД1-1РУ+4С :: cвойства||Window"):
        move(u"Автоопрос||CheckBox")
        move(u"Сохранить в БД||CheckBox")
        move(u"Отправлять трапы||CheckBox")
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window"):
        left_click(u" МД1-1РУ+4С :: cвойства||Window->Отменить||Button")
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"Полоса частот||TreeItem")
        right_click(u"56МГц ||TreeItem")

with Window(u"||Menu"):
    move(u"Обновить (F5)||MenuItem")
    move(u"Изменить||MenuItem")
    move(u'Переименовать||MenuItem')
    move(u"Добавить на карту||MenuItem")
    left_click(u"Свойства||MenuItem")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->Полоса частот||Window"):
        left_click(u"Автоопрос||CheckBox")
        left_click(u"Сохранить в БД||CheckBox")
        left_click(u"Контроль значения||CheckBox")
        left_click(u"Отменить||Button")

    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"BER 1с, QPSK||TreeItem")
        right_click(u"0  [/1.0E-06]||TreeItem#[0,0]")

with Window(u"||Menu"):
    move(u"Обновить (F5)||MenuItem")
    move(u'Переименовать||MenuItem')
    move(u"Добавить на карту||MenuItem")
    left_click(u"Свойства||MenuItem")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->BER 1с, QPSK||Window"):
        left_click(u"Автоопрос||CheckBox")
        left_click(u"Сохранить в БД||CheckBox")
        left_click(u"Контроль значения||CheckBox")
        left_click(u"Отменить||Button")

    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"BER 15мин||TreeItem")
        right_click(u"0  [/4.0E-06]||TreeItem#[1,0]")

with Window(u"||Menu"):
    move(u"Обновить (F5)||MenuItem")
    move(u"Добавить на карту||MenuItem")
    left_click(u"Свойства||MenuItem")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->BER 15мин, ствол 1||Window"):
        left_click(u"Автоопрос||CheckBox")
        left_click(u"Сохранить в БД||CheckBox")
        left_click(u"Контроль значения||CheckBox")
        left_click(u"Отменить||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")
