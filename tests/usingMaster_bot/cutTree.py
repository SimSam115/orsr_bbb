import sys, os, time
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot
import pyautogui

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
player.resetCamera()
player.selectThing("inventory")

while False:
    player.selectThing("tinderbox")
    player.selectThing("oak_log")
    time.sleep(3)
