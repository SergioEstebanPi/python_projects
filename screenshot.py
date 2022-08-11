# pip3 install virtualenv
# virtualenv projectsenv
# pip3 install pyautogui

import pyautogui
import time

def screenshot():
    name = int(round(time.time() * 1000))
    name = './screenshots_data/{}.png'.format(name)
    time.sleep(5)
    img = pyautogui.screenshot(name)
    img.show()
    
screenshot()