import time

import pyautogui
from pywinauto_recorder.player import *

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Список пользователей||Button")

with Window(u"Список пользователей||Window"):
    left_click(u"Создать пользователя Enter||Button")

with Window(u"Создать пользователя||Window"):
    left_click(u"Ок Enter||Button")
    left_click(u"Ошибка||Window->||Group->OK Enter||Button")
    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    send_keys('абвгдеёжзийклмнопрстуфхцчшщъыьэюя')
    left_click(u"Ок Enter||Button")
    left_click(u"Ошибка||Window->||Group->OK Enter||Button")
    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('BACKSPACE')

    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    send_keys('1234567890')
    left_click(u"Ок Enter||Button")
    left_click(u"Ошибка||Window->||Group->OK Enter||Button")
    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('BACKSPACE')

    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    send_keys('!@#$%^&*()-=')
    left_click(u"Ок Enter||Button")
    left_click(u"Ошибка||Window->||Group->OK Enter||Button")
    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('BACKSPACE')

    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    send_keys('admin3256')
    left_click(u"Ок Enter||Button")
    left_click(u"Ошибка||Window->||Group->OK Enter||Button")
    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('BACKSPACE')

    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    send_keys('qwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbnmqwertyuiopasdfghjklzxcvbq')
    left_click(u"Ок Enter||Button")
    left_click(u"Ошибка||Window->||Group->OK Enter||Button")
    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    pyautogui.hotkey('ctrl', 'a')
    time.sleep(1)
    pyautogui.hotkey('BACKSPACE')

    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    send_keys('user123')
    with Region(u"Пароль||Group"):
        left_click(u"Пароль||Edit#[0,0]")
        send_keys('123')
    left_click(u"Ок Enter||Button")
    left_click(u"Ошибка||Window->||Group->OK Enter||Button")
    with Region(u"Пароль||Group"):
        left_click(u"Пароль||Edit#[1,0]")
        send_keys('123')
    left_click(u"Ок Enter||Button")

pyautogui.moveTo(1118, 545)
pyautogui.click()
with Window(u"Удалить пользователя||Window"):
    with Region(u"||Group"):
        left_click(u"Да Alt+Д||Button")
with Window(u"Список пользователей||Window"):
    left_click(u"Закрыть Enter||Button")


