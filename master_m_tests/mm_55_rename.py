# MM-55 : Функция Переименовать
from pywinauto_recorder.player import *
import time
import pyautogui

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Создать карту||Button")

with Window(u"Новая карта||Window"):
    left_click(u"Создать Enter||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->||Pane->||Custom"):
        right_click(u"||Custom#[0,0]")
        send_keys('{DOWN} {ENTER}')

with Window(u"Создание сети||Window"):
    left_click(u" Вниз||ComboBox")
    time.sleep(1)
    send_keys('{UP} {ENTER}')
    left_click(u"Создать Enter||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->||Pane->||Custom"):
        double_left_click(u"||Custom#[0,0]")

with Window(u"Управление соединениями||Window"):
    left_click(u"Создать соединение Enter||Button")

with Window(u"Новое соединение||Window"):
    left_click(u"||Tree->||TreeItem#[0,1]")
    send_keys('172.17.130.111')
    left_click(u"||Spinner")
    send_keys('111')
    with Region(u"Автоопрос параметров||Group"):
        left_click(u"Автоопрос параметров||Spinner#[0,0]")
        pyautogui.mouseDown()
        pyautogui.move(-20, 0)
        pyautogui.mouseUp()
        send_keys('3')
    left_click(u"Ок Enter||Button")
with Window(u"Управление соединениями||Window"):
    left_click(u"Закрыть||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->||Pane->||Custom"):
        right_click(u"||Custom#[0,0]")
        time.sleep(1)
        pyautogui.move(10, 10, 1)
        pyautogui.click()
        time.sleep(2)

with Window(u"Подтверждение||Window"):
    send_keys("{ENTER}")
    time.sleep(15)

# проверяем кейс
pyautogui.moveTo(792, 300)
pyautogui.doubleClick()
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"МД1-1РУ+4С||TreeItem")
        pyautogui.click()
        time.sleep(3)
        pyautogui.hotkey('*')
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||TitleBar"):
        left_click(u"Закрыть||Button")
        pyautogui.moveTo(780, 342)
        pyautogui.doubleClick()

# выбираем в меню Переименовать
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"0  [/1.0E-06]||TreeItem#[2,0]")
        right_click(u"0  [/1.0E-06]||TreeItem#[2,0]")

with Window(u"||Menu"):
    left_click(u"Переименовать||MenuItem")
    right_click(u"Переименовать||MenuItem")
    send_keys('test')
with Window(u"BER 1с, QPSK :: Новое имя||Window"):
    with Region(u"||Group"):
        left_click(u"Установить Enter||Button")

# возвращаем название
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"0  [/1.0E-06]||TreeItem#[2,0]")
        right_click(u"0  [/1.0E-06]||TreeItem#[2,0]")

with Window(u"||Menu"):
    left_click(u"Переименовать||MenuItem")
    right_click(u"Переименовать||MenuItem")
    send_keys('{BACKSPACE}')
with Window(u"test :: Новое имя||Window"):
    with Region(u"||Group"):
        left_click(u"Установить Enter||Button")
        pyautogui.moveTo(558, 52)
        pyautogui.click()

# закрываем карту
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")