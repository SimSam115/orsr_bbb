import sys, os, time
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot
import pyautogui

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

#player.bankWith2ItemCraft("clay","water-bucket",count=14)


player.resetCamera()
time.sleep(0.5)
player.selectThing("fishing",offset=[-5,4])
player.clickMouse("down",spaces = 2,mouseType='right')
