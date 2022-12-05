from pywinauto.application import Application
from pywinauto_recorder.player import *
import time

with Window(u"||Pane"):
	left_click(u"Пуск||Button#[0,0]")

with Window(u"Начальный экран||Window"):
	with Region(u"||Window->Представление закреплений||List->Заголовок группы Группа Master M||Group"):
		left_click(u"Master M||ListItem")
		time.sleep(30)

#app = Application(backend="win32").connect(path = r"C:\MasterM\master.exe")
#with Window(u"Автораскрытие сети||Window"):
#	left_click(u"Прочитать адрес||Button")






