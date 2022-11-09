import pywhatkit
import pyautogui
from tkinter import *
import time as t
from datetime import datetime 
import random
import sys, os

msgs = ['Sample1', 'Sample2', 'Sample3']

def send(number, msg):

    dt = datetime.now()

    win = Tk() 
    screen_width = win.winfo_screenwidth() 
    screen_height= win.winfo_screenheight() 
    pywhatkit.sendwhatmsg(number, f'Il messaggio automatizzato è : {msg}', dt.hour, (dt.minute + 1), 15, True, 3)
    t.sleep(3)
    pyautogui.moveTo(screen_width * 0.694, screen_height* 0.964) 
    pyautogui.click() 
    pyautogui.press('enter') 

def main():
    with open('numeri.txt') as f:
        for line in f:
            while(True):
                try:
                    send(line, random.choice(msgs))
                except KeyboardInterrupt:
                    print('Interrupted')
                    try:
                        sys.exit(0)
                    except SystemExit:
                        os._exit(0)    
                except:
                    print('error, retrying')
                    t.sleep(3)
                break
    try:
        os.remove('PyWhatKit_DB.txt')
    except:
        print(':)')
    print('Terminato')

if __name__ == '__main__':
    main()



