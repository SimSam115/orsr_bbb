import sys, os, time, pyautogui
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
#player.selectThing("bank")
#player.resetCamera()
#player.bankWith2ItemCraft("clay","water-bucket",count=14,report=True)
#player.bankWith2ItemCraft("dough","dish",count=14,report=False)

def whatSpace():
    x, y = pyautogui.position()
    offset = [x-player.screen.left,y-player.screen.top]
    print(offset)
    
    #
def bankToPottery():
    player.resetCamera()
    pos = [[635,154],[675,185],[684, 186],[684, 186],[660, 184]]
    times = [9,16,12,12,9]

    for i in range(0,5):
        player.clickMouse(pos = pos[i])
        time.sleep(times[i])
def potteryToBank():
    player.resetCamera()
    pos = [[679, 43],[678, 43],[674, 46],[652, 46],[703, 69]]
    times = [12,14,12,14,8]

    for i in range(0,5):
        player.clickMouse(pos = pos[i])
        time.sleep(times[i])
def getItems():
    player.selectThing("bank",offset=[0,-2])
    time.sleep(4)
    player.clickMouse("right",spaces=4,offset=[0,-4])
    time.sleep(1)
    player.selectThing("all")
    time.sleep(1)
    player.selectThing("soft_clay")
    time.sleep(1)
    player.selectThing("quit")


player.resetCamera()
getItems()
x = 1
while True:
    bankToPottery()
    player.selectThing("anvil",offset=[20,2])
    time.sleep(5)
    player.selectThing("soft_clay")
    time.sleep(1)
    player.clickMouse("right",spaces=2,offset=[0,-10])
    time.sleep(1)
    player.simulateKey('2')
    canCraft = True
    while canCraft:
        time.sleep(3)
        canCraft = player.selectThing("soft_clay",click=False)
        if player.selectThing("levelup"):
            player.selectThing("soft_clay")
            player.clickMouse("right",spaces=2,offset=[0,-10])
            player.simulateKey('2')
            
        
    player.clickMouse("down",spaces=3,offset=[-60,0])
    time.sleep(3)
    player.simulateKey('2')
    
    canCraft = True
    while canCraft:
        time.sleep(3)
        canCraft = player.selectThing("undried_dish",click=False)
        if player.selectThing("levelup"):
            player.clickMouse("down",spaces=1)
            player.simulateKey('2')
    potteryToBank()
    player.selectThing("bank",offset=[0,-2])
    time.sleep(6)
    player.clickMouse("right",spaces=4)
    time.sleep(1)
    player.selectThing("empty")
    player.selectThing("soft_clay")
    time.sleep(1)
    player.selectThing("quit")
    
#player.textMaster("Water buckets are filled")



#while not player.selectThing("photos/water.png"): print("trying water")
#time.sleep(2)
#while not player.selectItem("photos/empty-bucket.png"): print("trying bucket")
#player.clickMouse(d="left",spaces=6,offset=[0,-10])