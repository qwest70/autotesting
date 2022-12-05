# в настройках есть функция, при двойном клике на станции открыть параметры или свойства
from pywinauto_recorder.player import *
import time
import pyautogui

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())

# ставим галку Открыть свойства
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||Custom"):
        left_click(u"||Button")

with Window(u""):
    left_click(u"||Menu")
    pyautogui.move(0, 25, 0.5)
    pyautogui.click()

with Window(u"Настройки||Window"):
    left_click(u"||List->Интерфейс||ListItem")
    pyautogui.move(300, 300, 1)
    pyautogui.scroll(-500)
    left_click(u"||Pane->||Custom->||Custom->||Custom->Поведение||Group->Открыть свойства||RadioButton")
    left_click(u"Сохранить Enter||Button")

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

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->||Pane->||Custom"):
        right_click(u"||Custom#[0,0]")

# проверяем наш кейс
pyautogui.moveTo(792, 300)
pyautogui.doubleClick()

with Window(u"Свойства станции||Window"):
    left_click(u"||Edit->||Custom")
    left_click(u"Сохранить Enter||Button")

# ставим галку Открыть свойства
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||Custom"):
        left_click(u"||Button")

with Window(u""):
    left_click(u"||Menu")
    pyautogui.move(0, 25, 0.5)
    pyautogui.click()

with Window(u"Настройки||Window"):
    left_click(u"||List->Интерфейс||ListItem")
    pyautogui.move(300, 300, 1)
    pyautogui.scroll(-500)
    left_click(u"||Pane->||Custom->||Custom->||Custom->Поведение||Group->Открыть параметры||RadioButton")
    left_click(u"Сохранить Enter||Button")

# проверяем кейс
pyautogui.moveTo(792, 300)
time.sleep(2)
pyautogui.doubleClick()

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window"):
        left_click(u"||TitleBar")

    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||TitleBar"):
        left_click(u"Закрыть||Button")

# закрываем карту
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")

