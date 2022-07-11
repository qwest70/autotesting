# Ошибка чтения адреса IP, IP2COM, СОМ порта если по адресу нет станции
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
    send_keys('1.1.1.1')

with Window(u"Новое соединение||Window"):
    left_click(u"Прочитать адрес||Button")
time.sleep(5)

with Window(u"Ошибка||Window"):
    with Region(u"||Group"):
        left_click(u"OK Enter||Button")
# IP2COM
with Window(u"Новое соединение||Window"):
    with Region(u"||Tree"):
        left_click(u"||TreeItem#[3,1]")
        send_keys('1.1.1.1')

with Window(u"Новое соединение||Window"):
    left_click(u"Прочитать адрес||Button")
time.sleep(5)

with Window(u"Ошибка||Window"):
    with Region(u"||Group"):
        left_click(u"OK Enter||Button")

# COM
pyautogui.moveTo(1000, 342)
pyautogui.scroll(-150)
pyautogui.moveTo(793, 410)
pyautogui.click()


with Window(u"Новое соединение||Window"):
    left_click(u"Прочитать адрес||Button")
    left_click(u"")
    time.sleep(5)

with Window(u"Ошибка||Window"):
    with Region(u"||Group"):
        left_click(u"OK Enter||Button")

with Window(u"Новое соединение||Window"):
    left_click(u"Отменить Enter||Button")

with Window(u"Управление соединениями||Window"):
    left_click(u"Закрыть||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")