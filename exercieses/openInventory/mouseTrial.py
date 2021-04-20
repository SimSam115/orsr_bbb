import pyautogui, pygetwindow, time

screen = pygetwindow.getWindowsWithTitle('Old School RuneScape')[0]
centerRatio = (2.8,2.8)
def move(direction,spaces):
    vel = [0,0]
    if direction == "up":    vel[1] =  0.32;
    if direction == "down":  vel[1] = -0.32;
    if direction == "left":  vel[0] =  0.3;
    if direction == "right": vel[0] = -0.3;
    print(vel)
    newRatio = (centerRatio[0] + (vel[0] * spaces),centerRatio[1] + (vel[1] * spaces))
    pyautogui.click(screen.left + (screen.width/newRatio[0]),screen.top+(screen.height/newRatio[1]))
    time.sleep(1.5)


#


while True:
    boxs = list(pyautogui.locateAllOnScreen("miniTree.png"))
    box = boxs[len(boxs)//2]
    if box:
        pyautogui.click(box)
        #tinder = pyautogui.locateCenterOnScreen("tinderbox.png")
        #pyautogui.click(tinder)
        time.sleep(7)
        move("left",1)
        time.sleep(3)
        #print("found")
    
