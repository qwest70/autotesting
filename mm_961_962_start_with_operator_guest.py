import pyautogui
import time
# import subprocess
# pyautogui.FAILSAFE = True
#
# def start_master(): #запуск программы
#     cmd = 'C:\MasterM\master.exe'
#     PIPE = subprocess.PIPE
#     p = subprocess.Popen(cmd, shell = True)
#     time.sleep(25) #ждем окно авторизации

from pywinauto.application import Application
from pywinauto_recorder.player import *
import time
with open('version.txt') as file:
    version = str(file.readline())
with open('version_operator.txt') as file:
    version_operator = str(file.readline())
with open('version_guest.txt') as file:
    version_guest = str(file.readline())
with Window(u"||Pane"):
    left_click(u"Пуск||Button#[0,0]")
with Window(u"Начальный экран||Window"):
    with Region(u"||Window->Представление закреплений||List->Заголовок группы Группа Master M||Group"):
        left_click(u"Master M||ListItem")
        time.sleep(30)
def pause():
    pyautogui.PAUSE = 0.5

# operator
with Window(u"Авторизация||Window"):
    left_click(u" Вниз||ComboBox")
    for _ in range(3):
        send_keys("{DOWN}")
    send_keys("{ENTER}")
    left_click(u"||Edit")
    send_keys('operator')
    left_click(u"Войти Enter||Button")
    time.sleep(15)

#выход из мастера
with Window(u"СПО \"Мастер М\" " + version_operator + u"||Window"):
    with Region(u"||TitleBar"):
        left_click(u"Закрыть||Button")
with Window(u"СПО \"Мастер М\" " + version_operator + u"||Window"):
    with Region(u"Завершение работы СПО \"Мастер М\"||Window"):
        left_click(u"Завершить работу Enter||Button")
        time.sleep(3)

# start_master()
with Window(u"||Pane"):
    left_click(u"Пуск||Button#[0,0]")

with Window(u"Начальный экран||Window"):
    with Region(u"||Window->Представление закреплений||List->Заголовок группы Группа Master M||Group"):
        left_click(u"Master M||ListItem")
        time.sleep(30)

# guest
with Window(u"Авторизация||Window"):
    left_click(u" Вниз||ComboBox")
    for _ in range(2):
        send_keys("{DOWN}")
    send_keys("{ENTER}")
    left_click(u"||Edit")
    send_keys('guest')
    left_click(u"Войти Enter||Button")
    time.sleep(15)

#выход из мастера
with Window(u"СПО \"Мастер М\" " + version_guest + u"||Window"):
    with Region(u"||TitleBar"):
        left_click(u"Закрыть||Button")
with Window(u"СПО \"Мастер М\" " + version_guest + u"||Window"):
    with Region(u"Завершение работы СПО \"Мастер М\"||Window"):
        left_click(u"Завершить работу Enter||Button")
