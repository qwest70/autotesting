import pyautogui

pyautogui.moveTo(1880, 520)
pyautogui.click(button='right')
pyautogui.moveTo(1770, 600)
pyautogui.click()
pyautogui.moveTo(728, 486)
pyautogui.click()
pyautogui.moveTo(977,515)
pyautogui.click()
pyautogui.hotkey('Ctrl', 'a')
pyautogui.hotkey('delete')
pyautogui.typewrite('abcd')
pyautogui.moveTo(1072, 576)
pyautogui.click()
pyautogui.screenshot('wrong_way_substray.png', region=(705, 408, 500, 200))
pyautogui.hotkey('ESC')

