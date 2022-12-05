# кейс проверяет, что вопрос при удалении сообщений появляется, если есть галка в настройках
from pywinauto_recorder.player import *
import time
import pyautogui

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())

# проверяем, что вопрос есть
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Custom->||SplitButton->||CheckBox")
    with Region(u"||Window->||Custom->||Pane->||Custom->||Table"):
        try:
            right_click(u"Значение параметра вернулось в норму||DataItem#[0,0]")
        except TimeoutError:
            right_click(u"Карта закрыта||DataItem#[0,0]")

pyautogui.move(50, 0, 0.5)
pyautogui.move(0, 110, 0.5)
pyautogui.click()

with Window(u"Удаление всех сообщений||Window"):
    with Region(u"||Group"):
        left_click(u"Нет Alt+Н||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Custom->||SplitButton->||CheckBox")

# ставим галку Не спрашивать при удалении всех сообщений
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||Custom"):
        left_click(u"||Button")

with Window(u""):
    left_click(u"||Menu")
    pyautogui.move(0, 25, 0.5)
    pyautogui.click()

with Window(u"Настройки||Window"):
    left_click(u"||List->Интерфейс||ListItem")
    left_click(u"||Pane->||Custom->||Custom->||Custom->Журналы||Group->Не спрашивать при удалении выбранных сообщений||CheckBox")
    left_click(u"Сохранить Enter||Button")

# проверяем, что сообщения нет
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Custom->||SplitButton->||CheckBox")
    with Region(u"||Window->||Custom->||Pane->||Custom->||Table"):
        try:
            right_click(u"Значение параметра вернулось в норму||DataItem#[0,0]")
        except TimeoutError:
            right_click(u"Карта закрыта||DataItem#[0,0]")

pyautogui.move(50, 0, 0.5)
pyautogui.move(0, 50, 0.5)
pyautogui.click()

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Custom->||SplitButton->||CheckBox")

# убираем галку, возвращаем в исходное состояние
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||Custom"):
        left_click(u"||Button")

with Window(u""):
    left_click(u"||Menu")
    pyautogui.move(0, 25, 0.5)
    pyautogui.click()

with Window(u"Настройки||Window"):
    left_click(u"||List->Интерфейс||ListItem")
    left_click(u"||Pane->||Custom->||Custom->||Custom->Журналы||Group->Не спрашивать при удалении выбранных сообщений||CheckBox")
    left_click(u"Сохранить Enter||Button")