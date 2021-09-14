
import pyautogui
import time


pyautogui.FAILSAFE = False

Position = (0, 0)

pyautogui.moveTo(Position)

Move_Position = pyautogui.position()

while Position == Move_Position:
  
  try:
    pyautogui.press('capslock')
    time.sleep(2)
    pyautogui.press('capslock')
    time.sleep(2)
    Move_Position = pyautogui.position()
    
  except:
    print("The Loop is Done")
    break




