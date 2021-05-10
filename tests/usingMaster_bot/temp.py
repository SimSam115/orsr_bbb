import sys, os, time, pyautogui,datetime
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

while True:
    while not player.selectThing("spells/high_alch"): time.sleep(0.1)
    time.sleep(0.1)
    player.clickMouse(pos = [738, 331])