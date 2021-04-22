import sys, os, time
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#player.selectThing("bank")
#player.resetCamera()
#player.bankWith2ItemCraft("clay","water-bucket",count=14,report=True)
player.bankWith2ItemCraft("dough","dish",count=14,report=True)