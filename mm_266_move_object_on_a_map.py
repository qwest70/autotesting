# перемещение объектов на карте
from pywinauto_recorder.player import *
import time
import pyautogui

with open('version.txt') as file:
    version = str(file.readline())

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
    left_click(u"||Spinner")
    send_keys('{UP}')
    left_click(u"Ок Enter||Button")

with Window(u"Управление соединениями||Window"):
    left_click(u"Закрыть||Button")

# перемещаем и удаляем сеть
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->||Pane->||Custom"):
        left_click(u"||Custom#[0,0]")
        time.sleep(1)
        send_keys('{VK_SHIFT down}')
        time.sleep(1)
        pyautogui.click()
        time.sleep(1)
        send_keys('{VK_SHIFT up}')
        time.sleep(1)
        pyautogui.dragTo(1500, 500, button='left' )
        pyautogui.hotkey('delete')
        pyautogui.hotkey('enter')


