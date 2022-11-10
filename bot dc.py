import pyautogui as auto
import time

time.sleep(5)


while True :
    auto.write('EKO')
    auto.press('enter')
    time.sleep(3)

pyautogui.FailSafeException = True

