import pyautogui
import time

def prevent_away():
    try:
        while True:
            
            pyautogui.move(6, 0)
            pyautogui.move(-5, 1)
            
            pyautogui.click()
            
            time.sleep(30)
    except KeyboardInterrupt:
        print("Program stopped.")

if __name__ == "__main__":
    prevent_away()

