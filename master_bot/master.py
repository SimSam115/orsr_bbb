import random, pygetwindow, pyautogui, time,sys, math
from random import random as r
def rr(area=4): return (r()*area - area/2)
from twilio.rest import Client
import sys, os, time

class Bot:
    def __init__(self,scriptDIR):
        self.dir = scriptDIR 
        self.center = [296, 220]
        self.masterPhone = Client("AC57db9e7ab173796dd3376ae134fb4d5e","f870aceb106c4505d5c7de3d58d893dc")
        while True:
            try:
                self.screen = pygetwindow.getWindowsWithTitle('Old School RuneScape')[0]
                break
            except(IndexError):
                print("~~~~~~~~~PLEASE OPEN RUNESCAPE~~~~~~~~~~~")
                input("hit enter to continue after opening")
            
        
    def clickMouse(self,d = "none", spaces = 1,pos=[0,0],offset=[0,0], click = True, clickCount = 1,mouseType = "left"):
        if(d == "none" and spaces == 1 and pos == [0,0] and offset==[0,0]):
            print("NEEDS AN INPUT")
            return False
        if(pos != [0,0]):
            pyautogui.moveTo(self.screen.left + pos[0] + rr(),
                             self.screen.top  + pos[1] + rr(),
                             duration=(random.randint(8,15)/60))
            pyautogui.mouseDown(button = mouseType)
            time.sleep(random.randint(2,5)/90)
            pyautogui.mouseUp(button = mouseType)
            return True
        
        vel = [0,0]
        if d == "up":    vel[1] = -25;
        if d == "down":  vel[1] =  25;
        if d == "left":  vel[0] = -25;
        if d == "right": vel[0] =  25;
        newRatio = (self.center[0] + (vel[0] * spaces),self.center[1] + (vel[1] * spaces))
        pyautogui.moveTo(self.screen.left + newRatio[0] + offset[0] + rr(),
                         self.screen.top  + newRatio[1] + offset[1] + rr(),
                         duration=(random.randint(8,20)/13))
        if click:
            for i in range(0,clickCount):
                pyautogui.mouseDown(button = mouseType)
                time.sleep(random.randint(4,8)/10)
                pyautogui.mouseUp(button = mouseType)
        return True
    
    def resetCamera(self):
        pyautogui.click([self.screen.left + 594 + rr(), self.screen.top + 53 + rr()])
        self.selectThing("settings")
        time.sleep(random.randint(10,40)/30)
        pyautogui.click([self.screen.left + 611 + rr(), self.screen.top + 251 + rr()])
        time.sleep(random.randint(10,40)/30)
        pyautogui.click([self.screen.left + 689 + rr(), self.screen.top + 311 + rr()])
        time.sleep(random.randint(10,40)/30)
        pyautogui.click([self.screen.left + 738 + rr(), self.screen.top + 249 + rr()])
        time.sleep(random.randint(10,40)/30)
        pyautogui.click([self.screen.left + 738 + rr(), self.screen.top + 314 + rr()])
        
    
    def simulateKey(self,key):
        pyautogui.press(key)
    
    def getAllItems(self,itemName):
        items = pyautogui.locateAllOnScreen(self.dir + "/photos/" + itemName + ".png")
        return list(items);
        
    def selectThing(self,itemName,clickCount = 1, click = True, offset = [0,0],mouseType = "left"):
        item = pyautogui.locateCenterOnScreen(self.dir + "/photos/" + itemName + ".png")
        if(not item): return False
        
        x, y = pyautogui.position()
        to_x, to_y = [x-self.screen.left,y-self.screen.top]
        from_x, from_y = [item.x-self.screen.left,item.y-self.screen.top]
        
        distance = math.sqrt( (to_x - from_x)**2 + (to_y - from_y)**2 ) / random.randint(350,400)
        

        pyautogui.moveTo(item.x + offset[0] + rr(area=1.5),
                         item.y + offset[1] + rr(area=1.5),
                         duration=distance)
        pyautogui.moveTo(item.x + offset[0] + rr(area=0.5),
                         item.y + offset[1] + rr(area=0.5))
        if click:
            for i in range(0,clickCount):
                pyautogui.click(button = mouseType)
                time.sleep(r()*0.6)
        return True
    
    def bankWith2ItemCraft(self,item1, item2,count = 1,craftNum = 1, report = False):
        
        self.selectThing("inventory")
        self.clickMouse(d="up",spaces=2)
        self.selectThing("bank1item")
        
        while True:
            #checks if items exist
            if not self.selectThing(item1,click = False): break
            if not self.selectThing(item2,click = False): break
            
            # actual selection of items
            if not self.selectThing(item1,count): break
            time.sleep(0.4)
            if not self.selectThing(item2,count): break
            time.sleep(0.4)
            
            #Quit bank into main screen
            if not self.selectThing("quit"): break
            time.sleep(0.4)
            
            #Select items to craft
            if not self.selectThing(item1): break
            time.sleep(0.4)
            if not self.selectThing(item2): break
            time.sleep(1)
            
            if craftNum == 1:
                pyautogui.press('space')
            else: pyautogui.press(str(craftNum))
            time.sleep(count*1.4)
            
            self.clickMouse(d="up",spaces=2)
            time.sleep(0.3)
            if not self.selectThing("empty"): break
        
        if report: self.textMaster("Bot has finished making : " + item1 + " + " + item2)
        return True
    
    def dumpItem(self,item):
        full = True
        while full:
            item = pyautogui.locateCenterOnScreen(item)
            if item:
                pyautogui.keyDown('shift')
                pyautogui.mouseDown(item.x + rr(), item.y + rr())
                time.sleep(0.1)
                pyautogui.mouseUp(item.x + rr(), item.y + rr())
                pyautogui.keyUp('shift')
            else:
                full = False
    def whatSpace(self):
        x, y = pyautogui.position()
        offset = [x-self.screen.left,y-self.screen.top]
        return offset
    
    
    def walkPath(self,path,timing=[]):
        if timing == []:
            for i in path:
                timing.append(12.4)
                
        for i in range(0,len(path)):
            current = path[i]
            pyautogui.moveTo(self.screen.left + current[0] + rr(),
                             self.screen.top  + current[1] + rr())
            pyautogui.mouseDown()
            time.sleep(random.randint(4,12)/10)
            pyautogui.mouseUp()
            time.sleep(timing[i])
        
    def textMaster(self,what):
        self.masterPhone.messages.create(to="+12242219324",from_="+16362491215",body=what)