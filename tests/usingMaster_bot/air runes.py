import sys, os, time
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
time.sleep(2)
toAir = [[656, 172],[673, 186],[642, 160],[656, 160],[640, 160]]
toAirTimings = [15,12,12,12,12]
toBank = [[721, 58],[718, 57],[677, 43],[673, 45]]

time.sleep(0)
def main():
    player.resetCamera()
    player.selectThing("bank_f")
    time.sleep(1)
    player.clickMouse("down",spaces=0.4,offset=[0,-5])
    time.sleep(1)
    player.selectThing("bank1item")   
    time.sleep(0.5) 
    player.selectThing("empty")
    time.sleep(1)
    player.selectThing("air_talisman")
    time.sleep(1)
    
    player.selectThing("rune",clickCount=23)
    time.sleep(1)
    player.walkPath(toAir,toAirTimings)
    




main()