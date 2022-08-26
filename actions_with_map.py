# проверяем создание карты, сохранение, перезапись и закрытие карты

from pywinauto_recorder.player import *
import time
import pyautogui
import os

with open('version.txt') as file:
    version = str(file.readline())

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Custom->||SplitButton->||Custom->||Button")

with Window(u"||Menu"):
    #    left_click(u"Карты||MenuItem->||Создать карту")
    left_click(u"Карты||MenuItem")
    pyautogui.move(300, 0, 1)
    send_keys('{ENTER}')
    send_keys('test')
    send_keys('{ENTER}')

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->test||Tab"):
        left_click(u"test||TabItem")
        pyautogui.move(10, 0, 1)
        pyautogui.click()

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")

# проверка загрузки карты
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Загрузить карту||Button")

with Window(u"Загрузка карты||Window"):
    left_click(u" Вниз||ComboBox")
    time.sleep(1)
    send_keys("{DOWN}")
    time.sleep(1)
    send_keys("{ENTER}")
    left_click(u"Загрузить Enter||Button")
    time.sleep(10)

# проверка Сохранить как
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Custom->||SplitButton->||Custom->||Button")

with Window(u"||Menu"):
    left_click(u"Карты||MenuItem")
    pyautogui.move(300, 0, 1)
    pyautogui.move(0, 130, 1)
    send_keys('{ENTER}')
    send_keys('test')
    send_keys('{ENTER}' * 2) # умножаем на два, если просит перезаписать карту
    time.sleep(10)

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->test||Tab"):
        left_click(u"test||TabItem")
        pyautogui.move(10, 0, 1)
        pyautogui.click()

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")
        time.sleep(5)

# удаляем созданную карту
os.remove(path='C:/MasterM/maps/test.map')
