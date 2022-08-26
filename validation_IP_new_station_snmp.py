
from pywinauto_recorder.player import *
import time
import pyautogui
from pywinauto.application import Application

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())


# создание сети

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
        send_keys('{ENTER}')
        time.sleep(3)
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->||Pane->||Custom"):
            right_click(u"||Custom#[0,0]")
with Window(u"||Menu"):
    left_click(u"Добавить станцию||MenuItem")

with Window(u"Новая станция||Window"):
    left_click(u"IP адрес||Edit")
    send_keys('!@#$%^()*')
    left_click(u"Создать Enter||Button")
    left_click(u"IP адрес||Edit")
    send_keys('qwertyuiop[]asdfghjklzxcvbnm;,./')
    left_click(u"Создать Enter||Button")
    left_click(u"IP адрес||Edit")
    send_keys('йцукенгшщзхъфывапролджэячсмитьбю')
    left_click(u"Создать Enter||Button")
    left_click(u"IP адрес||Edit")
    send_keys('256')
    left_click(u"Создать Enter||Button")
    left_click(u"IP адрес||Edit")
    send_keys('.256')
    left_click(u"Создать Enter||Button")
    left_click(u"IP адрес||Edit")
    send_keys('.256')
    left_click(u"Создать Enter||Button")
    left_click(u"IP адрес||Edit")
    send_keys('.256')

    left_click(u"Порт||Spinner")
    send_keys('!@#$%^()*qwertyuiop[]asdfghjklzxcvbnm;,./йцукенгшщзхъфывапролджэячсмитьбю')
    left_click(u"Создать Enter||Button")


# закрываем карту
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")

