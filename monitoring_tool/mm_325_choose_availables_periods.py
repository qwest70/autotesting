import pyautogui
from pywinauto_recorder.player import *
import time

with open('C:/Users/kosov.as/PycharmProjects/autotest_master/version.txt') as file:
    version = str(file.readline())

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
	with Region(u"||Custom->||SplitButton->||Custom"):
		left_click(u"||Button")

with Window(u"||Menu"):
	left_click(u"Инструменты||MenuItem")
	pyautogui.moveTo(600, 116)
	pyautogui.click()

with Window(u"Текущая история мониторинга||Window"):
	with Region(u"||SplitButton->||SplitButton->||Custom->||Custom"):
		left_click(u"24 ч.||Button")

with Window(u"||Menu"):
	left_click(u"2 ч.||MenuItem")

with Window(u"Текущая история мониторинга||Window"):
	with Region(u"||SplitButton->||SplitButton->||Custom"):
		left_click(u"Загрузить список станций Enter||Button")
	with Region(u"||SplitButton->||SplitButton->||Custom->||Custom"):
		left_click(u"2 ч.||Button")

with Window(u"||Menu"):
	left_click(u"6 ч.||MenuItem")

with Window(u"Текущая история мониторинга||Window"):
	with Region(u"||SplitButton->||SplitButton->||Custom"):
		left_click(u"Загрузить список станций Enter||Button")
	with Region(u"||SplitButton->||SplitButton->||Custom->||Custom"):
		left_click(u"6 ч.||Button")

with Window(u"||Menu"):
	left_click(u"12 ч.||MenuItem")

with Window(u"Текущая история мониторинга||Window"):
	with Region(u"||SplitButton->||SplitButton->||Custom"):
		left_click(u"Загрузить список станций Enter||Button")
	with Region(u"||SplitButton->||SplitButton->||Custom->||Custom"):
		left_click(u"12 ч.||Button")

with Window(u"||Menu"):
	left_click(u"24 ч.||MenuItem")

with Window(u"Текущая история мониторинга||Window"):
	left_click(u"||SplitButton->||SplitButton->||Custom->Загрузить список станций Enter||Button")
	with Region(u"||TitleBar"):
		left_click(u"Закрыть||Button")