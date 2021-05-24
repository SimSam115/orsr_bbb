import sys, os, time, pyautogui,datetime
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#player.moveMouse(loc=[100,100])
player.searchGamescreen("food/swordfish_raw")
player.clickMouse(mouseType="right")
player.searchGamescreen("fishing/harpoon_option")
player.clickMouse()