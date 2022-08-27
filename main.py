import pyautogui

screen_width, screen_height = pyautogui.size()

with open("put_id_here.txt", "r") as f:
    id =  f.read()

while True:
    pyautogui.doubleClick("box.png")
    pyautogui.press("backspace")
    pyautogui.write(f"vote {id}")
    pyautogui.click("multiplayer.png")
    pyautogui.click("back.png")