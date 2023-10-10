import keyboard
import pyautogui
import time

stop_flag = True

def on_key_press(event):
    global stop_flag
    if event.name == "f8":
        stop_flag = not stop_flag
        if stop_flag:
            print("f8 pressed, start")
        else:
            print("f8 pressed, stop")
            
def normal():
    pyautogui.moveTo(1746, 767)
    pyautogui.click()
    pyautogui.moveTo(1730, 1017)
    pyautogui.click()
    pyautogui.moveTo(114,149)
    pyautogui.click()
    pyautogui.moveTo(118,221)
    pyautogui.click()
    

if __name__ == '__main__':
    # use f8 to start/stop
    keyboard.on_press(on_key_press)
    while True:
        # print("running")
        time.sleep(0.01)
        if not stop_flag:
            normal()



# from pynput import keyboard

# def on_press(key):
#     try:
#         print('按下按键：{0}'.format(key.char))
#     except AttributeError:
#         print('按下特殊按键：{0}'.format(key))

# def on_release(key):
#     print('松开按键：{0}'.format(key))

# with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
#     listener.join()
            
            





