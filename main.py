import time
from idle import getIdleSec
import pyautogui as p

# def auto_on_rf():
#     rf_on = 'rf_on.png'
#     rf_off = 'rf_off.png'
#     on_ext = p.locateCenterOnScreen('')
#     if on_ext:
#         time.sleep(180)
#     while True:
#         try:
#             off_ext = p.locateCenterOnScreen(rf_off)
#             p.moveTo(off_ext)
#             p.click()
time.sleep(15)
print(getIdleSec())