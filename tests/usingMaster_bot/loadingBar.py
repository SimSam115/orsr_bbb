import sys, os, time, pyautogui
PACKAGE_PARENT = '../..'
SCRIPT_DIR = os.path.dirname(os.path.realpath(os.path.join(os.getcwd(), os.path.expanduser(__file__))))
sys.path.append(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))
from master_bot.master import Bot as runeBot

#player = runeBot(os.path.normpath(os.path.join(SCRIPT_DIR, PACKAGE_PARENT)))

count = 0;maxCount = 1000
oldP = 0
while True:
    count+=1
    percent = round((count/1000)*100)
    loadingBar = "▓" * percent
    loadingBar += "░" * (100 - percent)
    if(oldP != percent):
        os.system('cls')
        print(loadingBar)
        time.sleep(0.01)
    if(count > maxCount): count = 0
    oldP = percent
    
    