#from pynput.mouse import Button, Controller
import pyautogui
import keyboard
import time, ast

time.sleep(3)
with open("log.txt", "r") as f:
#    mouse = Controller()
#    k = keyboard.Controller()
    macro = list(ast.literal_eval(f.read()))
    for item in macro:
        print(item)
        time.sleep(item[1])
        if item[2] == "click":
            x = item[0]["x"]
            y = item[0]["y"]
            pyautogui.moveTo(x, y)
            if item[0]["button"] == "left":
                pyautogui.click()
            else:
                pyautogui.click(button='right')
#            pyautogui.click(Button.left if item[0]["button"] == "left" else Button.right)
#            m.release(mouse.Button.left if item[0]["button"] == "left" else mouse.Button.right)
        elif item[2] == "key":
            keyboard.press_and_release(item[0])
#            k.press(str(item[0]))
#            k.release(str(item[0]))

