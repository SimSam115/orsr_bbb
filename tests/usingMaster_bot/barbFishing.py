import sys, os, time, pyautogui,datetime
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


def main():
    drop_roe()
    i = 0
    while True:
        i+=1
        print("Round " + str(i))
        findFishingSpot()
        while not wait_filled():
            findFishingSpot()
        processFish()
    
    

def findFishingSpot():
    player.clickMouse("",offset=[45,0],mouseType="right")
    if player.selectThing("fishing/use_option"):
        return True
    
    for i in range(150,-220,-50):
        player.clickMouse("",offset=[45,i],mouseType="right")
        if player.selectThing("fishing/use_option"):
            return True
    return False

def processFish():
    fishes = player.getAllItems("fishing/trout_leaping")
    for i in fishes:
        player.selectThing("knife")
        pyautogui.click(i,duration=0.2)
        
    time.sleep(0.5)
    drop_roe()
    
def drop_roe():
    pyautogui.keyDown("shift")
    roes = player.getAllItems("fishing/roe")
    for i in roes:
        pyautogui.click(i,duration=0.2)
    pyautogui.keyUp("shift")
def wait_filled():
    for i in range(0,45):
        if len(player.getAllItems("fishing/trout_leaping")) > 19:
            return True
        time.sleep(1)
    return False


main()