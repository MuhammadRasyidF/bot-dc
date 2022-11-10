import pyautogui as auto
import time
import numpy as np

time.sleep(5)

#selama nilai true, akan menampikan string Eko
while True :
    auto.write('EKO')
    auto.press('enter')
    time.sleep(3)

pyautogui.FailSafeException = True

