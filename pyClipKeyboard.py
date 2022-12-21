import pyperclip
import keyboard 
import time
import sys

file1 = open(file='text.txt', mode='r',encoding='utf-8')
lines = file1.readlines()
  

while True:
    try:
        globalCount = 1
        for line in lines:
            lineCount = 0
            print("Line {}: {}".format(globalCount, line.strip()))
            globalCount += 1
            pyperclip.copy(line.strip())
            while True:
                try: 
                    if keyboard.is_pressed('v'):
                        print('You pressed v')
                        time.sleep(0.5)
                        lineCount+=1
                        if lineCount >= 2:
                            print('Changing line')
                            break
                    elif keyboard.is_pressed('e'):
                        time.sleep(0.5)
                        raise SystemExit
                except:
                    break
    except:
        break


