import pyautogui
import time
from pywinauto_recorder.player import *
import time
import pyautogui
import subprocess
pyautogui.FAILSAFE = True
with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())
# def start_master(): #запуск программы
#     cmd = 'C:\MasterM\master.exe'
#     PIPE = subprocess.PIPE
#     p = subprocess.Popen(cmd, shell = True)
#     time.sleep(25) #ждем окно авторизации
def pause():
    pyautogui.PAUSE = 0.5
#
# start_master()
# #авторизация
# pyautogui.moveTo(1030, 510)
# pyautogui.click()
# pyautogui.typewrite('admin', 0.5)
# pyautogui.click(1000, 560, 1, 1, 'left')

#открываем карту
pyautogui.moveTo(225, 50)
pyautogui.click()
#загружаем карту
pyautogui.moveTo(920, 530)
pyautogui.click()
time.sleep(15)

#увеличиваем масштаб
pyautogui.moveTo(48, 130)
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left', x = 48, y = 110)
pyautogui.moveTo(48, 215)
pyautogui.click()
pause()
#уменьшаем масштаб
pyautogui.moveTo(48, 130)
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left', x = 48, y = 185)
pyautogui.moveTo(48, 215)
pyautogui.click()

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")


