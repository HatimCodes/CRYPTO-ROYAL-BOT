import pyautogui
import time
import keyboard
def playandplayagain():
    if pyautogui.locateOnScreen('Imgs/play.png'):
        pyautogui.click('Imgs/play.png',duration= 0.5)
    if pyautogui.locateOnScreen('Imgs/playagain.png'):
        pyautogui.click('Imgs/playagain.png',duration= 0.5)
def checkcolorbox(color):
    while pyautogui.locateOnScreen('Imgs/'+color+'.png', confidence=0.8) != None and keyboard.is_pressed('space') == False:
        playandplayagain()
        boxx, boxy = pyautogui.center(pyautogui.locateOnScreen('Imgs/'+color+'.png', confidence=0.8))
        pyautogui.doubleClick(boxx, boxy, duration=0.7)
        time.sleep(0.7)
        pyautogui.doubleClick(boxx, boxy, duration=0.7)
        playandplayagain()
while keyboard.is_pressed('space') == False :
    try:
        playandplayagain()
        checkcolorbox("red")
        checkcolorbox("green")
        checkcolorbox("blue")
    except Exception  as e:
        with open("logs.txt", "a") as g:
            g.write(str(e)+"\n")
