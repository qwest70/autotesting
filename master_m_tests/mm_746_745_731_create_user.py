from pywinauto_recorder.player import *
import time
import pyautogui

with open('version.txt') as file:
    version = str(file.readline())
with open('version_user.txt') as file:
    version_user = str(file.readline())
# создаем пользователя
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Список пользователей||Button")

with Window(u"Список пользователей||Window"):
    left_click(u"Создать пользователя Enter||Button")

with Window(u"Создать пользователя||Window"):
    with Region(u"Пользователь||Group"):
        left_click(u"Пользователь||Edit#[0,0]")
        send_keys('test')
    left_click(u"Пользователь||Group->Пользователь||Edit#[0,0]")
    with Region(u"Пароль||Group"):
        left_click(u"Пароль||Edit#[0,0]")
        send_keys('123')
    left_click(u"Пароль||Group->Пароль||Edit#[1,0]")
    send_keys('123')
    left_click(u"Ок Enter||Button")
with Window(u"Список пользователей||Window"):
    left_click(u"Закрыть||Button")

# меняем права пользователя
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||TitleBar")
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Список пользователей||Button")
with Window(u"Список пользователей||Window"):
    with Region(u"||Table"):
        left_click(u"||DataItem#[3,2],")
        pyautogui.moveTo(1085, 548, 0.5)
        pyautogui.click()

with Window(u"Редактирование пользователя||Window"):
    with Region(u"Пользователь||Group"):
        left_click(u"Пользователь Вниз||ComboBox")
        time.sleep(1)
        send_keys('{DOWN}')
        send_keys('{ENTER}')
    left_click(u"Ок Enter||Button")
    send_keys('{ENTER}')

#заходим под новым пользователем
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Сменить текущего пользователя||Button")

with Window(u"Сменить текущего пользователя||Window"):
    left_click(u" Вниз||ComboBox")
    time.sleep(1)
    send_keys('{DOWN}' * 3)
    send_keys("{ENTER}")
    left_click(u"||Edit")
    send_keys('123')
    left_click(u"Войти Enter||Button")

# возвращаемся в админку и удаляем пользователя
with Window(u"СПО \"Мастер М\" " + version_user + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Сменить текущего пользователя||Button")

with Window(u"Сменить текущего пользователя||Window"):
    left_click(u" Вниз||ComboBox")
    time.sleep(1)
    send_keys('{UP}' * 3)
    send_keys("{ENTER}")
    left_click(u"||Edit")
    send_keys('admin')
    left_click(u"Войти Enter||Button")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    left_click(u"||TitleBar")
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Список пользователей||Button")
with Window(u"Список пользователей||Window"):
    with Region(u"||Table"):
        left_click(u"||DataItem#[3,2],")
        pyautogui.moveTo(1120, 548, 0.5)
        pyautogui.click()
with Window(u"Удалить пользователя||Window"):
    with Region(u"||Group"):
        left_click(u"Да Alt+Д||Button")

with Window(u"Список пользователей||Window"):
    left_click(u"Закрыть Enter||Button")