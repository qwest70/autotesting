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
    left_click(u"24 ч.||MenuItem")

with Window(u"Текущая история мониторинга||Window"):
    with Region(u"||SplitButton->||SplitButton->||Custom"):
        left_click(u"Загрузить список станций Enter||Button")

with Window(u"Текущая история мониторинга||Window"):
    with Region(u"||SplitButton->||Custom->||Tree"):
        left_click(u"Устройства в офисе2||TreeItem")
        send_keys('{RIGHT}')
        left_click(u"Сеть 4||TreeItem")
        send_keys('{RIGHT}')
        left_click(u"Станция4\nМД1-1РУ+||TreeItem")
        send_keys('{RIGHT}')
        left_click(u"МД1-1РУ+||TreeItem")
        send_keys('{RIGHT}')
        left_click(u"Телеметрийные данные||TreeItem")
        send_keys('{RIGHT}')
        left_click(u"Ствол 1||TreeItem")
        send_keys('{RIGHT}')
        left_click(u"BER 15мин, ствол 1||TreeItem")
    send_keys('{SPACE}')
    with Region(u"||SplitButton"):
        triple_left_click(u"||Custom->||Tree->BER 15мин, ствол 1||TreeItem")
        left_click(u"||SplitButton->||Custom->Закрыть все графики||Button")
        left_click(u"||Custom->||Tree->BER 15мин, ствол 1||TreeItem")

with Window(u"Текущая история мониторинга||Window"):
    with Region(u"||TitleBar"):
        left_click(u"Закрыть||Button")