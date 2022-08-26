import pyautogui
import time

def timer():
    time.sleep(1)
pyautogui.moveTo(271, 60)
pyautogui.click()
timer()
pyautogui.moveTo(1042, 477) #список пользователей
pyautogui.click()
timer()
pyautogui.moveTo(1042, 514)  #выбираем первого
pyautogui.click()
timer()
pyautogui.moveTo(1007, 508) #поле пароль
pyautogui.click()
timer()
pyautogui.typewrite("guest", 0.2)
pyautogui.moveTo(982, 565)
pyautogui.click()
timer()

pyautogui.moveTo(271, 60)
pyautogui.click()
timer()
pyautogui.moveTo(1042, 477) #список пользователей
pyautogui.click()
timer()
pyautogui.moveTo(1042, 529)  #выбираем второго
pyautogui.click()
timer()
pyautogui.moveTo(1007, 508) #поле пароль
pyautogui.click()
timer()
pyautogui.typewrite("operator", 0.2)
pyautogui.moveTo(982, 565)
pyautogui.click()
timer()

pyautogui.moveTo(271, 60)
pyautogui.click()
timer()
pyautogui.moveTo(1042, 477) #список пользователей
pyautogui.click()
timer()
pyautogui.moveTo(1042, 500)  #выбираем второго
pyautogui.click()
timer()
pyautogui.moveTo(1007, 508) #поле пароль
pyautogui.click()
timer()
pyautogui.typewrite("admin", 0.2)
pyautogui.moveTo(982, 565)
pyautogui.click()
timer()
