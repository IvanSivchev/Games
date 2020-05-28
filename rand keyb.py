import sleep from time
import pyautogui
import random

KEYS = ['п', "а", "р", "г", "н", "щ", " ", "к", "ч", "х", "ж", "с", "т"]
number_of_clicks = 100

def random_type():
    sleep(5)
    while number_of_clicks != 0:
        key = random.choise(KEYS)
        pyautogui.typewrite(key)
        number_of_clicks -= 1

random_type()