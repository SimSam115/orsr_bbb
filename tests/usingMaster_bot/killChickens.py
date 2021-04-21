import sys, os, time, pyautogui, math
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#player.selectThing("bank")
#player.resetCamera()
#player.bankWith2ItemCraft("clay","water-bucket",count=14)
#player.bankWith2ItemCraft("dough","dish",count=14,report=False)
count = 5000
while count > 1:
    count+=1
    for i in range(0,3):
        player.selectThing("mobs/chickenCenter")
        time.sleep(1)
    time.sleep(5)
    for i in range(0,360,45):
        for dis in range(40,200,40):
            click_x = math.cos(i) * dis
            click_y = math.sin(i) * dis
            player.clickMouse(pos=[player.center[0] + click_y,player.center[1] + click_x],mouseType="right")
            time.sleep(0.1)
            if player.selectThing("mobs/chickenAttack"):
                time.sleep(10)
            else: pyautogui.click()

            
