import sys, os, time, pyautogui,datetime
from random import random as r
def rr(size=4): return r() *size - size/2
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))


def main():
    fishCount = [0,0,0]
    processFish(fishCount)
    i = 0
    while True:
        i+=1
        print("Round %3d => \n\tTotal Fish: %4d, Trout: %4d, Salmon: %4d, Sturgeon: %4d" %
              (i,sum(fishCount),fishCount[0],fishCount[1],fishCount[2]) )
    
        findFishingSpot()
        while not wait_filled():
            findFishingSpot()
        processFish(fishCount)
        

def findFishingSpot():
    direct = [-1,1]
    for i in range(4,175,24):
        for d in direct:
            player.clickMouse("",offset=[22,i * d],mouseType="right")
            if player.selectThing("fishing/use_option"):
                return True
            else: pyautogui.move(150 + rr(20),10+ rr(10),duration=0.2)

    return False

def processFish(fishCount):
    fish = getAllFish(count = fishCount,sort = True)
    for i in fish:
        player.selectThing("knife")
        center = [i.left + i.width/2 + rr(),
                  i.top + i.height/2 + rr()]
                  
        pyautogui.click(center[0],center[1],duration=0.15)
        
    time.sleep(0.5)
    drop_roe()
    
def drop_roe():
    roes = player.getAllItems("fishing/roe")
    caviar = player.getAllItems("fishing/caviar")
    drop = roes + caviar
    drop.sort(key= lambda e: (e.top*4 + e.left) )
    
    pyautogui.keyDown("shift")
    for i in drop:
        pyautogui.click(i,duration=0.2)
    pyautogui.keyUp("shift")
    
def wait_filled():
    oldCount = 0
    timeLeft = 8
    for i in range(0,60):
        fishCount = len(getAllFish())
        if oldCount == fishCount:
            timeLeft -= 1
        else: timeLeft = 10
        oldCount = fishCount
        
        if timeLeft <= 0:
            return False
        if fishCount > 17:
            return True
        time.sleep(0.5)
        #print("fishNow: %3d, oldFish: %3d, timeLeft: %2d, i: %d" %
        #      (fish,oldCount,timeLeft,i))
    return False

def getAllFish(count = [0,0,0],sort = False):
    fish1 = player.getAllItems("fishing/trout_leaping")
    count[0] += len(fish1)
    fish2 = player.getAllItems("fishing/salmon_leaping")
    count[1] += len(fish2)
    fish3 = player.getAllItems("fishing/sturgeon_leaping")
    count[2] += len(fish3)
    fish = (fish1 + fish2 + fish3)
    if sort: fish.sort(key= lambda e: (e.top*4 + e.left) )
    return fish
#wait_filled()
main()