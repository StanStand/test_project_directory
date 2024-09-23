import pyautogui
import time

def prevent_away():
    try:
        while True:
            # 移動滑鼠一個像素然後移回原位置
            pyautogui.move(6, 0)
            pyautogui.move(-5, 1)
            # 每隔 60 秒重複一次
            time.sleep(5)
    except KeyboardInterrupt:
        print("Program stopped.")

if __name__ == "__main__":
    prevent_away()
