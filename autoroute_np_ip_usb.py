from pywinauto_recorder.player import *
import pyautogui
import time
#import subprocess
pyautogui.FAILSAFE = True

def start_master(): #запуск программы
    cmd = 'C:\MasterM\master.exe'
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell = True)
    time.sleep(20) #ждем окно авторизации
def pause():
     pyautogui.PAUSE = 0.5
def read_address():
     with Window(u"Автораскрытие сети||Window"):
          left_click(u"Прочитать адрес||Button")

start_master()
#авторизация
pyautogui.moveTo(1030, 510)
pyautogui.click()
pyautogui.typewrite('admin', 0.2)
pyautogui.click(1000, 560, 1, 1, 'left')
time.sleep(10)
pyautogui.moveTo(580, 13)
pyautogui.click()


#создаем карту
pyautogui.moveTo(150, 50)
pyautogui.click()
pyautogui.moveTo(1100, 580)
pyautogui.click()
time.sleep(1)

#открываем окно Автораскрытие сети
pyautogui.moveTo(800, 500)
pyautogui.click(button='right')
pyautogui.moveTo(900, 615)
pyautogui.click()

#автораскрытие через ip
pyautogui.moveTo(892, 335)
pyautogui.click()
pyautogui.typewrite('172.17.130.111', 0.2)
read_address()
time.sleep(3)
pyautogui.moveTo(1020, 720)
pyautogui.click()
time.sleep(20)

#проверяем работу Контроль сети
pyautogui.moveTo(800, 500)
pyautogui.click(button='right')
pyautogui.moveTo(890, 510)
pyautogui.click()
pyautogui.moveTo(1051, 547)
pyautogui.click()
time.sleep(20)
pyautogui.screenshot('check_np_work.png', region=(760, 430, 400, 100))

#удаляем сеть
pyautogui.moveTo(800, 500)
pyautogui.click()
pyautogui.hotkey('delete')
pyautogui.moveTo(1050, 542) # Удалить сеть?
pyautogui.click()
time.sleep(15)

#открываем окно Автораскрытие сети
pyautogui.moveTo(800, 500)
pyautogui.click(button='right')
pyautogui.moveTo(900, 615)
pyautogui.click()

#автораскрытие через USB
with Window(u"Автораскрытие сети||Window"):
     left_click(u"||Tree->||TreeItem#[1,1]")
     left_click(u"Прочитать адрес||Button")
     drag_and_drop(u"Прочитать адрес||Button", u"Прочитать адрес||Button")
time.sleep(3)
pyautogui.moveTo(1020, 720)
pyautogui.click()
time.sleep(20)

#проверяем работу Контроль сети
pyautogui.moveTo(800, 500)
pyautogui.click(button='right')
pyautogui.moveTo(890, 510)
pyautogui.click()
pyautogui.moveTo(1051, 547)
pyautogui.click()
time.sleep(20)
pyautogui.screenshot('check_np_work_usb.png', region=(760, 430, 400, 100))

#удаляем сеть
pyautogui.moveTo(800, 500)
pyautogui.click()
pyautogui.hotkey('delete')
pyautogui.moveTo(1050, 540) # Удалить сеть?
pyautogui.click()


