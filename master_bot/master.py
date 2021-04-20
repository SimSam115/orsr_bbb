import random, pygetwindow, pyautogui, time,sys
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
            
        
    def clickMouse(self,d = "none", spaces = 1,pos=[0,0],offset=[0,0], click = True, clickCount = 1):
        if(d == "none" and spaces == 1 and pos == [0,0] and offset==[0,0]):
            print("NEEDS AN INPUT")
            return False
        if(pos != [0,0]):
            pyautogui.moveTo(screen.left + pos[0],screen.top + pos[1])
            pyautogui.mouseDown()
            time.sleep(random.randint(4,9)/10)
            pyautogui.mouseUp()
            return True
            
        
        
        vel = [0,0]
        if d == "up":    vel[1] = -25;
        if d == "down":  vel[1] =  25;
        if d == "left":  vel[0] = -25;
        if d == "right": vel[0] =  25;
        newRatio = (self.center[0] + (vel[0] * spaces),self.center[1] + (vel[1] * spaces))
        pyautogui.moveTo(self.screen.left + newRatio[0] + offset[0],self.screen.top+newRatio[1] + offset[1])
        if click:
            for i in range(0,clickCount):
                pyautogui.mouseDown()
                time.sleep(random.randint(4,9)/10)
                pyautogui.mouseUp()
        return True
    
    def resetCamera(self):
        pyautogui.click([self.screen.left + 594, self.screen.top + 53])
    

    
    def selectThing(self,itemName,clickCount = 1, click = True):
        item = pyautogui.locateCenterOnScreen(self.dir + "/photos/" + itemName + ".png")
        if(not item): return False
        pyautogui.moveTo(item)
        if click:
            for i in range(0,clickCount):
                pyautogui.click()
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
            if craftNum == 2:
                pyautogui.press('2')
            if craftNum == 3:
                pyautogui.press('3')
            if craftNum == 4:
                pyautogui.press('4')
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
                pyautogui.mouseDown(item)
                time.sleep(0.1)
                pyautogui.mouseUp(item)
                pyautogui.keyUp('shift')
            else:
                full = False
    def textMaster(self,what):
        self.masterPhone.messages.create(to="+12242219324",from_="+16362491215",body=what)