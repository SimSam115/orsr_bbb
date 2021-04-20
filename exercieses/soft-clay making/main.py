import pyautogui, pygetwindow, time, random
from twilio.rest import Client



time.sleep(0)
screen = pygetwindow.getWindowsWithTitle('Old School RuneScape')[0]
center = [296, 220]

def main():
    message = True
    client = Client("AC57db9e7ab173796dd3376ae134fb4d5e","f870aceb106c4505d5c7de3d58d893dc")
    time.sleep(1)
    
    move('up',2)
    time.sleep(0.4)
    
    can = True
    while can:
        
        item = pyautogui.locateCenterOnScreen("clay.png")
        if(not item):
            can = False
            break
        pyautogui.click(item)
        
        item = pyautogui.locateCenterOnScreen("water-bucket.png")
        if(not item):
            can = False
            break
        pyautogui.click(item)    
        
        
        item = pyautogui.locateCenterOnScreen("close.png")
        pyautogui.click(item)
        time.sleep(0.5)
        
        item = pyautogui.locateCenterOnScreen("dough.png")
        pyautogui.click(item)
        item = pyautogui.locateCenterOnScreen("dish.png")
        pyautogui.click(item)
        
        time.sleep(0.7)
        pyautogui.press('space')
        time.sleep(16.5)
        
        move('up',2)
        time.sleep(0.3)
        item = pyautogui.locateCenterOnScreen("empty.png")
        pyautogui.click(item)
    
    if message:
        client.messages.create(to="+12242219324", 
                           from_="+16362491215", 
                           body="Bot has finished!")


def reset():
    moveMouse([594, 53])
    pyautogui.click()

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