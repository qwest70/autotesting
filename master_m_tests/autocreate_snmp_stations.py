from pywinauto_recorder.player import *
import time
with open('version.txt') as file:
    version = str(file.readline())

#
# with Window(u"СПО \"Мастер М\" " + version + u"||Window"):
#     with Region(u"||Custom->||Custom->||Pane->||Custom"):
#         right_click(u"||Custom#[0,0]")
#         send_keys('{DOWN} {ENTER}')
#
#     with Window(u"Создание сети||Window"):
#         send_keys('{ENTER}')
#         time.sleep(1)

k = 151
for i in range(51): # тут указываем нужное количество станций, но не более 130, т.к. после, иконки станций займут всё пространство карты
    with Window(u"Мастер М Версия: 0.0.0 beta (Administrator)||Window"):
        with Region(u"||Custom->||Custom->||Pane->||Custom"):
            right_click(u"||Custom#[0,0]")

    with Window(u"||Menu"):
        left_click(u"Добавить станцию||MenuItem")
    with Window(u"Новая станция||Window"):
        left_click(u"Имя||Edit")
        left_click(u"IP адрес||Edit")
        send_keys('192.168.0.' + str(k))
        k = 1 + k
        with Region(u"||Custom->||Custom->Community||Group"):
            left_click(u"Запись||Edit")
        left_click(u"||Custom->||Custom->Community||Group->Запись||Edit")
        send_keys('{BACKSPACE}' * 6)
        send_keys('private')
        left_click(u"Тип Вниз||ComboBox")
        time.sleep(1)
        send_keys('{DOWN}' * 18)
        time.sleep(1)
        send_keys('{ENTER}')


        left_click(u"Создать Enter||Button")

