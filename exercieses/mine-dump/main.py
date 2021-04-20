import pyautogui, pygetwindow, time, random, os

time.sleep(0)
screen = pygetwindow.getWindowsWithTitle('Old School RuneScape')[0]
centerRatio = (2.8,2.8)
#screen = pygetwindow.getWindowsWithTitle('Old School RuneScape')[0]
#pyautogui.click(screen.left + (screen.width/2), screen.top  + (screen.height/2))

def main():
    time.sleep(0.4)
    
    count = 750
    can = True;full = False
    while can:
        print(count)
        count-=1
        if(count < 0):
            item = pyautogui.locateCenterOnScreen("quit.png")
            pyautogui.click(item)
            time.sleep(1)
            os.system("shutdown /s /t 1");
        time.sleep(random.randint(25,35)/8)
        move("left",1)
        time.sleep(random.randint(25,35)/8)
        move("right",1)
        
        item = pyautogui.locateCenterOnScreen("bottom.png")
        if(not item):
            full = True
        
        while full:
            item = pyautogui.locateCenterOnScreen("iron.png")
            if item:
                pyautogui.keyDown('shift')
                pyautogui.mouseDown(item)
                time.sleep(0.1)
                pyautogui.mouseUp(item)
                pyautogui.keyUp('shift')
            else:
                full = False
        
        
        
    
    



def move(direction,spaces):
    vel = [0,0]
    if direction == "up":    vel[1] =  0.32;
    if direction == "down":  vel[1] = -0.32;
    if direction == "left":  vel[0] =  0.3;
    if direction == "right": vel[0] = -0.3;
    newRatio = (centerRatio[0] + (vel[0] * spaces),centerRatio[1] + (vel[1] * spaces))
    #pyautogui.click(screen.left + (screen.width/newRatio[0]),screen.top+(screen.height/newRatio[1]))
    pyautogui.moveTo(screen.left + (screen.width/newRatio[0]),screen.top+(screen.height/newRatio[1]))
    pyautogui.mouseDown()
    time.sleep(random.randint(4,9)/10)
    pyautogui.mouseUp()
    
    


main()
