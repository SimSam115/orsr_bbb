import sys, os, time
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

player.selectThing("bank",offset=[7,2])
time.sleep(2)
while True:
    player.clickMouse("down",spaces=0.5)
    time.sleep(0.5)
    player.selectThing("blast/steel")
    player.selectThing("furnace", offset=[-4.5,0])
    time.sleep(10.4)
    player.clickMouse("right",spaces=3)
    time.sleep(0.4)
    player.simulateKey("space")
    time.sleep(155)
    player.selectThing("bank",offset=[7,2])
    time.sleep(11)
