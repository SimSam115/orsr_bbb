import sys, os, time, pyautogui
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

player.resetCamera()
player.selectThing("bank",offset=[7,2])
time.sleep(2)
player.clickMouse("down",spaces=0.2,offset=[0,-4])
time.sleep(1)
player.selectThing("bank1item")
while True:
    player.selectThing("crafting/ring_mold")
    if not player.selectThing("gold",clickCount=13): break
    if not player.selectThing("crafting/sapphire",clickCount=13): break
    time.sleep(1)
    while not player.selectThing("furnace", offset=[-4,0]): time.sleep(1)
    time.sleep(10)
    player.clickMouse("right",spaces=3)
    time.sleep(1)
    player.selectThing("crafting/sapphire_ring")
    time.sleep(24)
    while not player.selectThing("bank",offset=[7,2]): time.sleep(1)
    time.sleep(12)
    player.clickMouse("down",spaces=0.5)
    player.selectThing("empty")
    time.sleep(1)

