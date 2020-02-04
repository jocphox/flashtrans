from PyQt5.QtWidgets import QApplication
from baiduapi2 import BaiduAPI
import keyboard
from PIL import ImageGrab, Image
import pyperclip
from datetime import datetime
from time import sleep
import time

def monitor():

    if keyboard.wait("ctrl+alt+z")==None:
        sleep(1)
        im=ImageGrab.grabclipboard()
        im.save("ImageGrab.png")
        print(time.time())
    # if keyboard.wait("ctrl+z") == None:
    #     exit()

if __name__=='__main__':
    import sys
    for _ in range(sys.maxsize):
        print("a")
        monitor()


