# MM-62 : Установка границ и их отображение возле значения числового параметра
from pywinauto_recorder.player import *
import time
import pyautogui
import os

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Создать карту||Button")

with Window(u"Новая карта||Window"):
    send_keys('{BACKSPACE}')
    left_click(u"||Edit#[1,0]")
    send_keys('1')
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

# раскрываем дерево и ставим диапазон - проверяем корректность отображения
pyautogui.moveTo(780, 342)
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

# проверяем основной кейс
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    try: # если температура не 38, пробуем 39
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"Температура МД||TreeItem")
            left_click(u"38 °C||TreeItem")
            right_click(u"38 °C||TreeItem")
    except TimeoutError:
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"Температура МД||TreeItem")
            left_click(u"39 °C||TreeItem")
            right_click(u"39 °C||TreeItem")
with Window(u"||Menu"):
    left_click(u"Свойства||MenuItem")
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window"):
        left_click(u"Контроль значения||CheckBox")
        pyautogui.moveTo(809, 481, 1)
        pyautogui.click()
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window->Контроль значения||CheckBox"):
        left_click(u"Контроль значения||Edit#[0,0]")
        send_keys('20')
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window"):
        left_click(u"Температура МД||Window->Сохранить||Button")
    try:
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"38 °C [20/]||TreeItem")
    except TimeoutError:
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"39 °C [20/]||TreeItem")
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    try: # если температура не 38, пробуем 39
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"Температура МД||TreeItem")
            left_click(u"38 °C [20/]||TreeItem")
            right_click(u"38 °C [20/]||TreeItem")
    except TimeoutError:
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"Температура МД||TreeItem")
            left_click(u"39 °C [20/]||TreeItem")
            right_click(u"39 °C [20/]||TreeItem")
with Window(u"||Menu"):
    left_click(u"Свойства||MenuItem")
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window->Контроль значения||CheckBox"):
        left_click(u"Контроль значения Enter||Button")
        left_click(u"Контроль значения||Edit#[1,0]")
        send_keys('40')
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window"):
        left_click(u"Температура МД||Window->Сохранить||Button")
try:
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        with Region(
                    u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"38 °C [/40]||TreeItem")
            time.sleep(2)
            right_click(u"38 °C [/40]||TreeItem")
    with Window(u"||Menu"):
        left_click(u"Свойства||MenuItem")
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        with Region(
                    u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window->Контроль значения||CheckBox"):
            left_click(u"Контроль значения||Button#[1,1]")
            pyautogui.moveTo(809, 481, 1)
            pyautogui.click()
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window"):
            left_click(u"Температура МД||Window->Сохранить||Button")
            pyautogui.moveTo(558, 52)
            pyautogui.click()
except TimeoutError:
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        with Region(
                    u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"39 °C [/40]||TreeItem")
            time.sleep(2)
            right_click(u"39 °C [/40]||TreeItem")
    with Window(u"||Menu"):
        left_click(u"Свойства||MenuItem")
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        with Region(
                    u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window->Контроль значения||CheckBox"):
            left_click(u"Контроль значения||Button#[1,1]")
            pyautogui.moveTo(809, 481, 1)
            pyautogui.click()
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window"):
            left_click(u"Температура МД||Window->Сохранить||Button")
            pyautogui.moveTo(558, 52)
            pyautogui.click()


# закрываем карту
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")

#проверка границ при загрузке карты
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Загрузить карту||Button")

with Window(u"Загрузка карты||Window"):
    # left_click(u"||TitleBar")
    # left_click(u" Вниз||ComboBox")
    # for _ in range(50):
    #     send_keys('{DOWN down}')
    # send_keys('{DOWN up}')
    # send_keys('{ENTER}')
    send_keys('{ENTER}')
    time.sleep(10)

pyautogui.moveTo(780, 342)
pyautogui.doubleClick()

# with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    # with Region(u"||Custom->||Custom->||Pane->||Custom"):
    #     double_left_click(u"||Custom")
    #     time.sleep(2)
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    try:
        with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"38 °C||TreeItem")
            right_click(u"38 °C||TreeItem")
    except TimeoutError:
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"39 °C||TreeItem")
            right_click(u"39 °C||TreeItem")

with Window(u"||Menu"):
    left_click(u"Свойства||MenuItem")
    pyautogui.moveTo(809, 481, 1)
    pyautogui.click()
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(
                u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window->Контроль значения||CheckBox"):
        left_click(u"Контроль значения||Edit#[0,0]")
        send_keys('20')
        left_click(u"Контроль значения||Edit#[1,0]")
        send_keys('40')
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window"):
        left_click(u"Температура МД||Window->Сохранить||Button")
        pyautogui.moveTo(558, 49, 1)
        pyautogui.click()

# переоткрываем карту
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Загрузить карту||Button")

with Window(u"Загрузка карты||Window"):
    # left_click(u"||TitleBar")
    # left_click(u" Вниз||ComboBox")
    # for _ in range(50):
    #     send_keys('{DOWN down}')
    # send_keys('{DOWN up}')
    # send_keys('{ENTER}')
    send_keys('{ENTER}')
    time.sleep(10)

pyautogui.moveTo(780, 342)
pyautogui.doubleClick()
time.sleep(2)

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    try:
        with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"38 °C [20/40]||TreeItem")
            right_click(u"38 °C [20/40]||TreeItem")
    except TimeoutError:
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"39 °C [20/40]||TreeItem")
            right_click(u"39 °C [20/40]||TreeItem")

pyautogui.moveTo(560, 49, 1)
pyautogui.click()
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")
        time.sleep(2)

path = "C:/MasterM/maps/1.map"
os.remove(path)




