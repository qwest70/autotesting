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
     left_click(u"||List->Интеграция по SNMP||ListItem")
     left_click(u"||Pane->||Custom->||Custom->||Custom->Включить отправку SNMP-трапов||CheckBox->Отправлять SNMP-трапы при изменении доступности станции")
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

# отключаем станцию и смотрим в журнал
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    pyautogui.moveTo(780, 342)
    pyautogui.rightClick()
with Window(u"||Menu"):
    left_click(u"Остановить обслуживание||MenuItem")

with Window(u"Остановить обслуживание||Window"):
    left_click(u"Остановить Enter||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
     with Region(u"||Custom"):
        left_click(u"||SplitButton->||CheckBox")


with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Window->||Custom->||Pane->||Custom-> Настройки журнала||Button")
    with Region(u"Настройки журнала||Window"):
        left_click(u"Выберите настройки||Group->Показать системные сообщения||CheckBox")
    left_click(u"Настройки журнала||Window->Ок Enter||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Window->||Custom->||Pane->||Custom"):
        left_click(u"||Table->Отправлен SNMP-трап доступности станции, oid=1.3.6.1.4.1.19707.10.101.1||DataItem")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    pyautogui.moveTo(780, 342)
    pyautogui.rightClick()
with Window(u"||Menu"):
    left_click(u"Возобновить обслуживание||MenuItem")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Window->||Custom->||Pane->||Custom"):
        left_click(u"||Table->Отправлен SNMP-трап доступности станции, oid=1.3.6.1.4.1.19707.10.101.1||DataItem")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||Window->||Custom->||Pane->||Custom-> Настройки журнала||Button")
    with Region(u"Настройки журнала||Window"):
        left_click(u"Выберите настройки||Group->Показать системные сообщения||CheckBox")
    left_click(u"Настройки журнала||Window->Ок Enter||Button")
    with Region(u"||Custom"):
        left_click(u"||SplitButton->||CheckBox")




# закрываем карту
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")

# убираем галку
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||Custom"):
        left_click(u"||Button")

with Window(u""):
    left_click(u"||Menu")
    pyautogui.move(0, 25, 0.5)
    pyautogui.click()

with Window(u"Настройки||Window"):
     left_click(u"||List->Интеграция по SNMP||ListItem")
     left_click(u"||Pane->||Custom->||Custom->||Custom->Включить отправку SNMP-трапов||CheckBox->Отправлять SNMP-трапы при изменении доступности станции")
     left_click(u"Сохранить Enter||Button")