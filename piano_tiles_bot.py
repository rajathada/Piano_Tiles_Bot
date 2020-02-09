import pyautogui
import time
from mss import mss

start_x = 500
start_y = 400

#X-Cordinates for each tile
cord_x = [0,100,200,299]

bbox = (start_x, start_y, start_x+300,start_y+1)
#
# def test_time():
#     with mss() as sct:
#         t1 = time.time()
#         for i in range(100):
#             img = sct.grab(bbox)
#             # pyautogui.click(2,300)
#         t2 = time.time()
#         print(t2-t1)
#
# test_time()
#
#
# def print_mouse_position():
#     # pyautogui.displayMousePosition()
#     while True:
#         print(pyautogui.position())
#         time.sleep(1)
#
#
# print_mouse_position()

def start():
    with mss() as sct:
        while True:
            img = sct.grab(bbox)
            # print(img.pixels)
            for cord in cord_x:
                # print(img.pixel(cord, 0))
                if img.pixel(cord, 0)[0] < 100:
                    pyautogui.click(start_x+cord, start_y)
                    break
time.sleep(2)
start()