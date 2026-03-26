import pyautogui
import pygetwindow as gw
import time
import subprocess
from datetime import datetime

pyautogui.FAILSAFE = True  # move mouse to top-left to emergency stop

def auto_study_log():
    today = datetime.now().strftime("%d-%m-%Y")
    day   = datetime.now().strftime("%A")
    time_now = datetime.now().strftime("%I:%M %p")

    log_content = f"""
============================================
  DAILY STUDY LOG — {today} ({day})
============================================

Time Started  : {time_now}
Student       : Manoj Kumar (BCA Data Science)
GitHub        : github.com/nx-manoj

--------------------------------------------
TODAY'S TASKS
--------------------------------------------
[ ] Python Practice       — 1 hour
[ ] LeetCode DSA          — 2 problems
[ ] ML / GenAI Study      — 1 hour
[ ] Project Work          — 1 hour
[ ] Revision              — 30 mins

--------------------------------------------
NOTES
--------------------------------------------
Write your notes here...


--------------------------------------------
COMPLETED TODAY
--------------------------------------------



============================================
"""

    print("Opening Notepad...")
    subprocess.Popen(["notepad.exe"])
    time.sleep(1.5)  # wait for Notepad to open

    # Find and activate the Notepad window
    wins = gw.getWindowsWithTitle("Notepad")
    if not wins:
        print("Notepad not found!")
        return
    wins[0].activate()
    time.sleep(0.5)

    print("Typing study log...")
    pyautogui.click()  # click inside Notepad
    time.sleep(0.3)

    # Type the content
    for line in log_content.split('\n'):
        pyautogui.typewrite(line, interval=0.01)
        pyautogui.press('enter')

    time.sleep(0.5)

    # Save with Ctrl+S
    print("Saving file...")
    pyautogui.hotkey('ctrl', 's')
    time.sleep(1.5)

    # In Save dialog — type filename
    filename = f"StudyLog_{today}.txt"
    pyautogui.typewrite(filename, interval=0.05)
    pyautogui.press('enter')

    print(f"Done! Saved as {filename}")

if __name__ == "__main__":
    print("Starting in 3 seconds... switch to desktop!")
    time.sleep(3)
    auto_study_log()