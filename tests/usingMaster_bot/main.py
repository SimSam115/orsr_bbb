import sys, os, time
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(SCRIPT_DIR)
#player.selectThing("bank")
#player.resetCamera()
player.bankWith2ItemCraft("clay","water-bucket",count=14)
#player.bankWith2ItemCraft("dough","dish",count=14,report=False)

while False:
    player.selectThing("bank")
    time.sleep(11)
    player.clickMouse("right",spaces=4)
    time.sleep(1)
    player.selectThing("empty")
    time.sleep(0.5)

    if not player.selectThing("empty-bucket",clickCount=28): break
    player.selectThing("quit")

    player.selectThing("water")
    time.sleep(10)

    player.selectThing("empty-bucket")
    player.clickMouse("up",spaces=3)
    time.sleep(14)
#player.textMaster("Water buckets are filled")

#while not player.selectThing("photos/water.png"): print("trying water")
#time.sleep(2)
#while not player.selectItem("photos/empty-bucket.png"): print("trying bucket")
#player.clickMouse(d="left",spaces=6,offset=[0,-10])