import pyautogui
from pywinauto.application import Application
from pywinauto_recorder.player import *

with open('version.txt') as file:
    version = str(file.readline())

# проверяем открыт ли журнал, если не открыт, то открываем

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Custom->||SplitButton->||CheckBox")
try:
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        left_click(u"||Window->||Custom->||Pane->||Custom-> Настройки журнала||Button")
        send_keys("{ENTER}")
except TimeoutError:
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        left_click(u"||Custom->||SplitButton->||CheckBox")

pyautogui.moveTo(900, 781)
pyautogui.click(button='right')  # жмякаем ПКМ на сообщении
pyautogui.moveTo(991, 774)
pyautogui.click()  # выбираем пункт Пометить как прочитанное
pyautogui.moveTo(900, 781)
pyautogui.click(button='right')
pyautogui.moveTo(991, 774)
pyautogui.click()  # Пометить как непрочитанное
pyautogui.moveTo(900, 781)
pyautogui.click(button='right')
pyautogui.moveTo(991, 804)
pyautogui.click()  # Пометить все как прочитанное
pyautogui.moveTo(900, 781)
pyautogui.click(button='right')
pyautogui.moveTo(991, 804)
pyautogui.click()  # Пометить все как непрочитанное
pyautogui.moveTo(900, 781)
pyautogui.click(button='right')  # жмякаем ПКМ на сообщении
pyautogui.moveTo(991, 834)
pyautogui.click()  # Удалить
pyautogui.moveTo(1038, 538)  # подтверждаем Да
pyautogui.click()
# проверяем фильтры важности сообщений
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Window->||Custom->||Pane->||Custom->||Custom"):
        left_click(u"||CheckBox#[0,0]")
        left_click(u"||CheckBox#[0,1]")
        left_click(u"||CheckBox#[0,2]")
        left_click(u"||CheckBox#[0,0]")
        left_click(u"||CheckBox#[0,1]")
        left_click(u"||CheckBox#[0,2]")
# Настройки журнала
pyautogui.moveTo(1675, 960)
pyautogui.click()
pyautogui.moveTo(847, 511)
pyautogui.click(clicks=2)
pyautogui.moveTo(847, 540)
pyautogui.click(clicks=2)
pyautogui.hotkey('Enter')

# проверка фильтра по источнику
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Window->||Custom->||Pane->||Custom"):
        left_click(u"Фильтр журнала||Button")

with Window(u"Фильтр журнала||Window"):
    with Region(u"Выберите выражение источника||Group"):
        left_click(u"Использовать фильтр по источнику||CheckBox")
        left_click(u"Выберите выражение источника||Edit")
    send_keys('{VK_LCONTROL down}'
              '{a}'
              '{VK_LCONTROL up}'
              'some')
    #	    double_left_click(u"")
    left_click(u"Ок||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Window->||Custom->||Pane->||Custom"):
        left_click(u" Фильтр журнала||Button")

with Window(u"Фильтр журнала||Window"):
    left_click(u"Выберите выражение источника||Group->Использовать фильтр по источнику||CheckBox")
    left_click(u"Ок||Button")


# проверка фильтра по событию
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Window->||Custom->||Pane->||Custom"):
        left_click(u"Фильтр журнала||Button")

with Window(u"Фильтр журнала||Window"):
    with Region(u"Выберите выражение события||Group"):
        left_click(u"Использовать фильтр по событию||CheckBox")
        left_click(u"Выберите выражение события||Edit")
    send_keys('{VK_LCONTROL down}'
              '{a}'
              '{VK_LCONTROL up}'
              'some')
    #	    double_left_click(u"")
    left_click(u"Ок||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Window->||Custom->||Pane->||Custom"):
        left_click(u" Фильтр журнала||Button")

with Window(u"Фильтр журнала||Window"):
    left_click(u"Выберите выражение события||Group->Использовать фильтр по событию||CheckBox")
    left_click(u"Ок||Button")

pyautogui.moveTo(1882, 63)
pyautogui.click()
