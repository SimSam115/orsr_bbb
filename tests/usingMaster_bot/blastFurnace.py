import sys, os, time
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


def main():
    #player.resetCamera()
    getItems()
    
    player.selectThing("anvil",offset=[13,18])
    time.sleep(12)
    player.clickMouse("right",2)
    player.selectThing("blast/bag",mouseType="right")
    player.selectThing("blast/empty_bag")
    player.clickMouse("right",2)
    
    player.selectThing("anvil",offset=[0,35])
    time.sleep(5)
    player.clickMouse("right",2.2,offset=[0,-25])
    time.sleep(0.6)
    player.simulateKey("2")
    time.sleep(0.1)
    player.simulateKey("space")
    time.sleep(1)
    
    player.selectThing("water",offset=[24,0])
    time.sleep(7.7)
    
    player.clickMouse("down",1)
    player.clickMouse("",pos=[695, 259])

def checkFillBucket():
    if(player.selectThing("empty_bucket")):
        player.selectThing("water",offset=[-1,-8])
        time.sleep(5)
        player.clickMouse("down",1)
        
    

def getItems():
    time.sleep(0.2)
    player.selectThing("blast/coal")
    player.selectThing("quit")
    player.selectThing("blast/bag")
    player.clickMouse("down",1)
    time.sleep(0.4)
    player.selectThing("blast/iron")
    player.selectThing("quit")
    
    



player.clickMouse("down",1)
for i in range(1,10):
    print("Currently running round "+ str(i))
    main()