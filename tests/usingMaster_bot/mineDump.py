import sys, os, time, pyautogui,datetime
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot



player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


def main():
    time.sleep(0.4)
    
    can = True;full = False
    while can:

        player.clickMouse("left",2)
        time.sleep(1)
        player.clickMouse("right",4)
        time.sleep(4)
        
        full = not player.selectThing("bottom",click=False)
        if full: pyautogui.keyDown('shift')
        while full:
            item = player.selectThing("iron")
            if item:
                pyautogui.mouseDown()
                time.sleep(0.1)
                pyautogui.mouseUp()
            else:
                pyautogui.keyUp('shift')
                full = False
                
main()
        