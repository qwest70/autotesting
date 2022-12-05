from pywinauto_recorder.player import *
from pywinauto.application import Application
from pywinauto.controls.win32_controls import ComboBoxWrapper
import time

with open('version.txt') as file:
    version = str(file.readline())

#app = Application(backend="win32").start('C:\MasterM\master.exe')
#app = Application(backend="win32").connect(process=5324) # если подключиться к процессу
#dlg_login = app.MasterM # describe the window inside MasterM.exe process
#actionable_dlg = dlg_login.wait('visible') # wait till the window is really open
#dlg_login = Application(backend="win32").connect(path = r"C:\MasterM\master.exe")

# запуск через меню Пуск
with Window(u"||Pane"):
    left_click(u"Пуск||Button#[0,0]")

with Window(u"Начальный экран||Window"):
    with Region(u"||Window->Представление закреплений||List->Заголовок группы Группа Master M||Group"):
        left_click(u"Master M||ListItem")
        time.sleep(30)
#dlg_spec = app.window(title = "Авторизация")
#dlg_spec.app["Авторизация"].print_control_identifiers() #показывает типо некоторые виджеты

#guest
# with Window(u"Авторизация||Window"):
# 	left_click(u" Вниз||ComboBox")
# 	time.sleep(2)
# 	send_keys("{DOWN}")
# 	send_keys("{ENTER}")
# 	left_click(u"||Edit")
# 	send_keys('guest')
#admin
with Window(u"Авторизация||Window"):
    left_click(u"||Edit")
    send_keys('admin')
    left_click(u"Войти Enter||Button")
    time.sleep(15)
try:
    with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
        with Region(u"||TitleBar"):
            left_click(u"Развернуть||Button")
except TimeoutError:
    send_keys('{ESC}')


# попытка авторизации через обращение к виджетам напрямую, пока не работает
# dlg_combobox = app["Авторизация"]["Down"].WrapperObject()
# combo = ComboBoxWrapper(dlg_combobox)
# combo.Select("Guest")
#dlg_login.minimize()

# еще попытка через список ролей
# with open('list_version.txt') as file:
#     roles = str(file.readline())
# for m in roles:
#     version = str(m)
#     try:
#         with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
#             with Region(u"||TitleBar"):
#                 left_click(u"Развернуть||Button")
#     except TimeoutError:
#         continue





