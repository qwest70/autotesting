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

k = 207
for i in range(51): # тут указываем нужное количество станций, но не более 130, т.к. после, иконки станций займут всё пространство карты
    with Window(u"Master M Version: 0.0.0 beta (Administrator)||Window"):
        with Region(u"||Custom->||Custom->||Pane->||Custom"):
            right_click(u"||Custom#[0,0]")

    with Window(u"||Menu"):
        left_click(u"Add station||MenuItem")
    with Window(u"New station||Window"):
        left_click(u"Name||Edit")
        left_click(u"IP address||Edit")
        send_keys('192.168.0.' + str(k))
        k = 1 + k
        with Region(u"||Custom->||Custom->Community||Group"):
            left_click(u"Write||Edit")
        left_click(u"||Custom->||Custom->Community||Group->Write||Edit")
        send_keys('{BACKSPACE}' * 6)
        send_keys('private')
        left_click(u"Type Вниз||ComboBox")
        time.sleep(1)
        send_keys('{DOWN}' * 18)
        time.sleep(1)
        send_keys('{ENTER}')


        left_click(u"Create Enter||Button")

