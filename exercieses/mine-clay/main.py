import pyautogui, pygetwindow, time, random

time.sleep(0)
screen = pygetwindow.getWindowsWithTitle('Old School RuneScape')[0]
center = [296, 220]
def main():
    selectBank()
    bankItems()
    while True:
        reset()
        bankToMine()
        digRocks(20)
        mineToBank()
        selectBank()
        bankItems()
        
        
def bankItems():
    move("right",2)
    moveMouse([654, 262])
    pyautogui.click()
    time.sleep(1)
    moveMouse([519, 57])
    pyautogui.click()
    
    
def reset():
    moveMouse([594, 53])
    pyautogui.click()
    
def digRocks(count):
    while True:
        for i in range(0,5):
            move("left",2)
            time.sleep(1.45)
            move("up",1)
            time.sleep(1.45)
        item = pyautogui.locateCenterOnScreen("bottom.png")
        if not item: break
def whatSpace():
    x, y = pyautogui.position()
    offset = [x-screen.left,y-screen.top]
    print(offset)
    
def bankToMine():
    reset()
    pos = [[626, 151],[672, 186],[690, 179],[698, 168],[662, 146]]
    times = [9,12,10,9,8]

    for i in range(0,5):
        moveMouse(pos[i])
        pyautogui.click()
        time.sleep(times[i])
def mineToBank():
    pos = [[660, 48],[657, 45],[675, 49],[709, 70]]
    times = [12,12,11,8]

    for i in range(0,4):
        moveMouse(pos[i])
        pyautogui.click()
        time.sleep(times[i])
    
    selectBank()
def selectBank():
    reset()
    item = pyautogui.locateCenterOnScreen("bank.png")
    
    pyautogui.click(item.x,item.y + 20)
    time.sleep(3)
def moveMouse(offset):
    pyautogui.moveTo(screen.left + offset[0],screen.top+ offset[1])

def move(direction,spaces):
    vel = [0,0]
    if direction == "up":    vel[1] = -25;
    if direction == "down":  vel[1] =  25;
    if direction == "left":  vel[0] = -25;
    if direction == "right": vel[0] =  25;
    newRatio = (center[0] + (vel[0] * spaces),center[1] + (vel[1] * spaces))
    #pyautogui.click(screen.left + (screen.width/newRatio[0]),screen.top+(screen.height/newRatio[1]))
    pyautogui.moveTo(screen.left + newRatio[0],screen.top+newRatio[1])
    pyautogui.mouseDown()
    time.sleep(random.randint(4,9)/10)
    pyautogui.mouseUp()
    
    


main()