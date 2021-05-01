import sys, os, time, pyautogui,datetime
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot



player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
start = datetime.datetime.now()
print(start)


#player.resetCamera()
player.selectThing("bank",offset=[7,2])
time.sleep(3)
player.clickMouse("down",spaces=0.2,offset=[0,-4])
time.sleep(1)
player.selectThing("bank1item")
while True:
    player.selectThing("crafting/ring_mold")
    if not player.selectThing("gold",clickCount=13): break
    if not player.selectThing("crafting/emerald",clickCount=13): break
    time.sleep(1)
    while not player.selectThing("furnace", offset=[-4.5,0]):
        time.sleep(1)
    time.sleep(10)
    player.clickMouse("right",spaces=3)
    time.sleep(1)
    test = -1
    while not player.selectThing("crafting/emerald_ring"):
        player.selectThing("furnace", offset=[-4.5,0])
        time.sleep(7)
        player.clickMouse("right",spaces=3+test)
        test+=0.2
        if test > 1:
            assert("I missed the furance")
            
    time.sleep(24)
    while not player.selectThing("bank",offset=[7,2]): time.sleep(1)
    time.sleep(12)
    player.clickMouse("down",spaces=0.5)
    
    while not player.selectThing("top"):
        player.selectThing("empty")
    time.sleep(1)
    
end = datetime.datetime.now()
print(end - start)

player.textMaster("Im done making rings. It took me:" + str(end - start))

