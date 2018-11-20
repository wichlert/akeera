'''
Created on Nov 20, 2018

@author: akeera
'''

import pyautogui
i=1
print(pyautogui.position())
pyautogui.PAUSE = 2.5
while i < 10:
 pyautogui.click(x=100, y=200)
 pyautogui.PAUSE = 2.5
 pyautogui.click(x=200, y=200)
 i += 1