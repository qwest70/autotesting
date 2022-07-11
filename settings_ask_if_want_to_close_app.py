# кейс проверяет, что вопрос при выходе, если есть галка в настройках
from pywinauto_recorder.player import *
import time
import pyautogui

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||Custom"):
        left_click(u"||Button")

with Window(u""):
    left_click(u"||Menu")
    pyautogui.move(0, 25, 0.5)
    pyautogui.click()

with Window(u"Настройки||Window"):
    left_click(u"||List->Интерфейс||ListItem")
    left_click(u"||Pane->||Custom->||Custom->||Custom->Базовые||Group->Подтверждение выхода||CheckBox")
    left_click(u"Сохранить Enter||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||TitleBar"):
        left_click(u"Закрыть||Button")
        time.sleep(10)

with Window(u"||Pane"):
    left_click(u"Пуск||Button#[0,0]")

with Window(u"Начальный экран||Window"):
    with Region(u"||Window->Представление закреплений||List->Заголовок группы Группа Master M||Group"):
        left_click(u"Master M||ListItem")
        time.sleep(30)

#admin
with Window(u"Авторизация||Window"):
    left_click(u"||Edit")
    send_keys('admin')
    left_click(u"Войти Enter||Button")
    time.sleep(15)


with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||Custom"):
        left_click(u"||Button")

with Window(u""):
    left_click(u"||Menu")
    pyautogui.move(0, 25, 0.5)
    pyautogui.click()

with Window(u"Настройки||Window"):
    left_click(u"||List->Интерфейс||ListItem")
    left_click(u"||Pane->||Custom->||Custom->||Custom->Базовые||Group->Подтверждение выхода||CheckBox")
    left_click(u"Сохранить Enter||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||TitleBar->Закрыть||Button")
    left_click(u"Завершение работы СПО \"Мастер М\"||Window->Не выходить||Button")