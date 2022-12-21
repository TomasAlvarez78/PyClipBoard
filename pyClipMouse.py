import pyperclip
from pynput import mouse
from pynput.mouse import Listener
from pynput.keyboard import Key, Controller
import time
import sys

file1 = open(file='text.txt', mode='r',encoding='utf-8')
lines = file1.readlines()
  
globalCount = 0           
lineCount = 0
keyboard = Controller()
copyButtons = [ mouse.Button.right, mouse.Button.x1, mouse.Button.x2 ]
buttonSelected = 1

# 0 - Right-Click 
# 1 - Bottom-Click
# 2 - Top-Click

def on_click(x, y, button, pressed):
    global globalCount
    global lineCount
    global keyboard
    global lateralButton
    global copyButtons
    global buttonSelected

    if pressed and button == copyButtons[buttonSelected]:
        print(globalCount)
        print(lineCount)
        print('{0} at {1}'.format(
            'Pressed' if pressed else 'Released',
            (x, y)))
        try:
            print("Line {}: {}".format(globalCount, lines[globalCount].strip()))
            pyperclip.copy(lines[globalCount])
            keyboard.press(Key.ctrl)
            keyboard.press('v')
            keyboard.release('v')
            keyboard.release(Key.ctrl)
            # keyboard.press(Key.enter)
            # keyboard.release(Key.enter)

            time.sleep(0.1)
            lineCount+=1
            if lineCount >= 2:
                print('Changing line')
                globalCount += 1
                lineCount = 0
            if globalCount >= len(lines):
                globalCount = 0
        except:
            return
    if pressed and button == mouse.Button.middle:
        return False                 

with Listener(on_click=on_click) as listener:
    listener.join()