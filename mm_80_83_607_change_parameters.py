from pywinauto_recorder.player import *
import pyautogui
import time
with open('version.txt') as file:
    version = str(file.readline())

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Загрузить карту||Button")

with Window(u"Загрузка карты||Window"):
    left_click(u"||TitleBar")
    left_click(u" Вниз||ComboBox")
    for _ in range(50):
        send_keys('{DOWN down}')
    send_keys('{DOWN up}')
    send_keys('{ENTER}')
    send_keys('{ENTER}')
    time.sleep(10)

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||Custom->||Pane->||Custom"):
        double_left_click(u"||Custom")
        time.sleep(2)
        pyautogui.scroll(-1000)
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"Вид резервирования||TreeItem")
        left_click(u"1+1,1ч ||TreeItem")
        right_click(u"1+1,1ч ||TreeItem")

with Window(u"||Menu"):
    left_click(u"Изменить||MenuItem")
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->Вид резервирования||Window"):
        left_click(u" Вниз||ComboBox")
        time.sleep(1)
        send_keys('{UP}')
        send_keys('{ENTER}')
        time.sleep(1)
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window"):
        left_click(u"Вид резервирования||Window->Установить Enter||Button")
        time.sleep(4)
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"Порт подключения||TreeItem")
        left_click(u"1 ||TreeItem#[0,0]")

    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"Вид резервирования||TreeItem")
        left_click(u"1+0 ||TreeItem")
        right_click(u"1+0 ||TreeItem")
with Window(u"||Menu"):
    left_click(u"Изменить||MenuItem")
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->Вид резервирования||Window"):
        left_click(u" Вниз||ComboBox")
        time.sleep(1)
        send_keys('{DOWN}')
        send_keys('{ENTER}')
        time.sleep(1)
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window"):
        left_click(u"Вид резервирования||Window->Установить Enter||Button")
        time.sleep(4)
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"Источник синхронизации||TreeItem")
        left_click(u"Авто ||TreeItem#[0,0]")
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"Частота ПРМ||TreeItem")
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"152300 кГц||TreeItem")
        right_click(u"152300 кГц||TreeItem")
with Window(u"||Menu"):
        left_click(u"Изменить||MenuItem")
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->Частоты||Window"):
        left_click(u"Обменять значения||Button")
        left_click(u"||Spinner#[0,0]")
        left_click(u"Установить Enter||Button")
        time.sleep(4)
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"252300 кГц||TreeItem")

    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        right_click(u"252300 кГц||TreeItem")
with Window(u"||Menu"):
    left_click(u"Изменить||MenuItem")
with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->Частоты||Window"):
        left_click(u"Обменять значения||Button")
        left_click(u"||Spinner#[0,0]")
        left_click(u"Установить Enter||Button")
        time.sleep(4)
    with Region(u"Сеть 4 :: Станция 111 [111] :: Доступна||Window->||Custom->||Pane->||Custom->||Custom->||Tree"):
        left_click(u"152300 кГц||TreeItem")

with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
    with Region(u"||Custom->||SplitButton->||ToolBar"):
        left_click(u"Закрыть карту||Button")

with Window(u"Закрыть карту||Window"):
    with Region(u"||Group"):
        left_click(u"Да Enter||Button")