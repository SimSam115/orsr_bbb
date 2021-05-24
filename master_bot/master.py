import random, pygetwindow, pyautogui, time,sys, math
from random import random as r
def rr(area=4): return (r()*area - area/2)
from twilio.rest import Client
import sys, os, time

mouseAlgo = ["none",pyautogui.easeInQuad,pyautogui.easeOutQuad,pyautogui.easeInOutQuad,pyautogui.easeInBounce,pyautogui.easeInElastic]


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
                try:
                    self.screen = pygetwindow.getWindowsWithTitle('OSBuddy Guest - Guest')[0]
                    break
                except(IndexError):
                    print("~~~~~~~~~PLEASE OPEN RUNESCAPE~~~~~~~~~~~")
                    input("hit enter to continue after opening")
    
    
    def moveMouse(self,loc):
        x, y = pyautogui.position()
        to_x, to_y = [x-self.screen.left,y-self.screen.top]
        from_x, from_y = loc
        offset_x, offset_y = [rr(area=125),rr(area=125)]
        
        
        distance = math.sqrt( (to_x - from_x)**2 + (to_y - from_y)**2 ) / random.randint(390,450)
        
        
        pyautogui.moveTo(loc[0] + offset_x, loc[1] + offset_y, distance*0.8,random.choice(mouseAlgo))
        #time.sleep(random.randint(10,30)/15)
        pyautogui.moveTo(loc[0],loc[1], duration=distance*0.1)
        
    def clickMouse(self,mouseType="left", clickCount=1 ):
        for i in range(0,clickCount):
            pyautogui.mouseDown(button=mouseType)
            time.sleep(random.randint(2,5)/90)
            pyautogui.mouseUp(button=mouseType)
            time.sleep(random.randint(2,5)/90)
        
    def moveCharacter(self,d, spaces = 1,offset=[0,0]):
       
        
        vel = [0,0]
        if d == "up":    vel[1] = -25;
        if d == "down":  vel[1] =  25;
        if d == "left":  vel[0] = -25;
        if d == "right": vel[0] =  25;
    
    def search(self,loc,itemName):
        area = (self.screen.left + loc[0],self.screen.top + loc[1],loc[2],loc[3])
        im = pyautogui.screenshot(region=area)
        
        item = pyautogui.locate(self.dir + "/photos/" + itemName + ".png",im)
        if(not item): return False
        pos = [area[0]+(item.left+(item.width/2)),area[1]+(item.top+(item.height/2))]
        
        self.moveMouse(loc = pos)
    
    def searchInventory(self,itemName):
        area = (553,239,182,252)
        self.search(area,itemName)
        
    def searchMinimap(self,itemName):
        area = (572,43,140,240)
        self.search(area,itemName)
        
    def searchGamescreen(self,itemName):
        area = (7,36,511,332)
        self.search(area,itemName)        
    
        
    
    def resetCamera(self):
        pyautogui.click([self.screen.left + 594 + rr(), self.screen.top + 53 + rr()])
        
    
    def simulateKey(self,key):
        pyautogui.press(key)
    
    def getAllItems(self,itemName):
        items = pyautogui.locateAllOnScreen(self.dir + "/photos/" + itemName + ".png")
        return list(items);
        
    
    def bankWith2ItemCraft(self,item1, item2,count = 1,craftNum = 1, report = False):
        
        if report: self.textMaster("Bot has finished making : " + item1 + " + " + item2)
        return True
    
                
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
            self.moveMouse(loc=current)
            time.sleep(timing[i])
        
    def textMaster(self,what):
        self.masterPhone.messages.create(to="+12242219324",from_="+16362491215",body=what)