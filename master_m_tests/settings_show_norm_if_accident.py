# кейс проверяет, что норма отображается в дереве параметров, когда есть авария
from pywinauto_recorder.player import *
import time
import pyautogui

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())
# ставим галку
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
    left_click(u"||Pane->||Custom->||Custom->||Custom->Аварии||Group->Показывать норму при аварии||CheckBox")
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

# with Window(u"||Menu"):
#     left_click(u"Опрос конфигурации станций сети||MenuItem")
#     time.sleep(15)

# открываем дерево параметров и создаем аварию

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
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"Температура МД||TreeItem")
        pyautogui.move(100, 0, 1)
        pyautogui.rightClick()

with Window(u"||Menu"):
    drag_and_drop(u"Обновить (F5)||MenuItem", u"Свойства||MenuItem")
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window"):
        pyautogui.moveTo(809, 481, 1)
        pyautogui.click()
    with Region(
            u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window->Контроль значения||CheckBox"):
        left_click(u"Контроль значения||Edit#[0,0]")
        send_keys('20')
    with Region(
            u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->Температура МД||Window->Контроль значения||CheckBox"):
        left_click(u"Контроль значения||Edit#[1,0]")
        send_keys('30')
    with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window"):
        left_click(u"Температура МД||Window->Сохранить||Button")
try:
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"38 °C [20/30]||TreeItem")
except:
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        with Region(u"Сеть 1 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
            left_click(u"39 °C [20/30]||TreeItem")
pyautogui.moveTo(250, 50)
pyautogui.mouseDown()
pyautogui.move(490, 50)
pyautogui.mouseUp()
# отключаем галку
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||Custom"):
        left_click(u"||Button")

with Window(u""):
    left_click(u"||Menu")
    pyautogui.move(0, 25, 0.5)
    pyautogui.click()

with Window(u"Настройки||Window"):
    left_click(u"||List->Интерфейс||ListItem")
    left_click(u"||Pane->||Custom->||Custom->||Custom->Аварии||Group->Показывать норму при аварии||CheckBox")
    left_click(u"Сохранить Enter||Button")

# закрываем карту
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")


