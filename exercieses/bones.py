import pyautogui, pygetwindow, time, random

time.sleep(1)
#screen = pygetwindow.getWindowsWithTitle('Old School RuneScape')[0]
#pyautogui.click(screen.left + (screen.width/2), screen.top  + (screen.height/2))

can = True
while can:
    item = pyautogui.locateCenterOnScreen("photos/bones.png")
    if item:
        pyautogui.mouseDown(item)
        time.sleep(random.randint(8,14)/10)
        pyautogui.mouseUp(item)
    else: can = False
