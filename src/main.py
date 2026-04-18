import time
import os
import sys
import pyautogui
import keyboard
from plyer import notification
from detector import find_target


# ---------------- PATH FIX FOR EXE ----------------
def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)


# ---------------- ASSETS ----------------
TARGET1 = resource_path("assets/target1.png")
TARGET2 = resource_path("assets/target2.png")
TARGET3 = resource_path("assets/target3.png")
TARGET4 = resource_path("assets/target4.png")

CAUTION1 = resource_path("assets/caution1.png")
CAUTION2 = resource_path("assets/caution2.png")
CAUTION3 = resource_path("assets/caution3.png")   # <-- ADD THIS


# ---------------- SETTINGS ----------------
CONFIDENCE = 0.8
START_DELAY = 5
WAIT_IF_FAIL = 5
STEP2_FIX_COOLDOWN = 10


running = False
last_step2_fix_time = 0


# ---------------- UTILITIES ----------------
def show_notification(title, message):
    try:
        notification.notify(title=title, message=message, timeout=3)
    except:
        pass


def toggle_bot():
    global running
    running = not running

    if running:
        print("\nBOT STARTED\n")
        show_notification("AutoClick Bot", "BOT STARTED")
    else:
        print("\nBOT STOPPED\n")
        show_notification("AutoClick Bot", "BOT STOPPED")


def smart_sleep(seconds):
    end_time = time.time() + seconds
    while time.time() < end_time:
        if not running:
            return False
        time.sleep(0.1)
    return True


def click_target4(reason=""):
    """Safely click target4 if found"""
    pos4 = find_target(TARGET4, CONFIDENCE)
    if pos4:
        pyautogui.click(pos4)
        print(f"target4 clicked {reason}: {pos4}\n")
        return True
    else:
        print("target4 not found while trying to click.\n")
        return False


keyboard.add_hotkey("ctrl+shift+alt+s", toggle_bot)

print("Program started.")
print("Press Ctrl+Shift+Alt+S to START/STOP bot.\n")


# ---------------- MAIN LOOP ----------------
while True:

    if not running:
        time.sleep(0.2)
        continue

    print("Session started... waiting 5 seconds")
    if not smart_sleep(START_DELAY):
        continue

    # ==================================================
    # 🔥 PRIORITY CHECK (CAUTION3 must override everything)
    # ==================================================
    if find_target(CAUTION3, CONFIDENCE):
        print("CAUTION3 detected! Clicking target4 (priority override).")
        click_target4("(due to CAUTION3)")
        continue

    # ---------------- CAUTION2 CHECK ----------------
    if find_target(CAUTION2, CONFIDENCE):
        print("CAUTION2 detected! Clicking target4...")
        click_target4("(due to CAUTION2)")
        continue

    # ---------------- STEP 1 ----------------
    pos1 = find_target(TARGET1, CONFIDENCE)

    if pos1:
        pyautogui.click(pos1)
        print("target1 found and clicked:", pos1)
    else:
        print("target1 not found -> going to step 2")

    if not running:
        continue

    # ==================================================
    # AGAIN CHECK CAUTION3 BEFORE NEXT STEP
    # ==================================================
    if find_target(CAUTION3, CONFIDENCE):
        print("CAUTION3 detected after step1! Clicking target4.")
        click_target4("(due to CAUTION3)")
        continue

    # ---------------- STEP 2 ----------------
    pos2 = find_target(TARGET2, CONFIDENCE)

    if pos2:
        pyautogui.click(pos2)
        print("target2 found and clicked:", pos2)
        print("Restarting session...\n")
        continue

    print("target2 not found.")

    current_time = time.time()

    if current_time - last_step2_fix_time >= STEP2_FIX_COOLDOWN:
        print("Running Step2 FIX (retry + force click)...")
        last_step2_fix_time = current_time

        start_time = time.time()
        pos2 = None

        while time.time() - start_time < 2:
            if not running:
                break

            # CAUTION3 priority during retry too
            if find_target(CAUTION3, CONFIDENCE):
                print("CAUTION3 detected during step2 retry! Clicking target4.")
                click_target4("(due to CAUTION3)")
                pos2 = None
                break

            pos2 = find_target(TARGET2, CONFIDENCE)
            if pos2:
                pyautogui.click(pos2)
                print("target2 found in retry and clicked:", pos2)
                print("Restarting session...\n")
                break

            time.sleep(0.2)

        if not pos2 and running:
            w, h = pyautogui.size()
            pyautogui.click((w // 2) + 500, (h // 2) - 100)
            print("Force clicked refresh position.")

            if not smart_sleep(0.5):
                continue

            if find_target(CAUTION3, CONFIDENCE):
                print("CAUTION3 detected after force click! Clicking target4.")
                click_target4("(due to CAUTION3)")
                continue

            pos2 = find_target(TARGET2, CONFIDENCE)
            if pos2:
                pyautogui.click(pos2)
                print("target2 found after force click. Clicked:", pos2)
                print("Restarting session...\n")
                continue

    else:
        print("Step2 FIX skipped (cooldown active).")

    print("target2 still not found -> going to step 3")

    if not running:
        continue

    # ==================================================
    # CAUTION3 PRIORITY BEFORE STEP3
    # ==================================================
    if find_target(CAUTION3, CONFIDENCE):
        print("CAUTION3 detected before step3! Clicking target4.")
        click_target4("(due to CAUTION3)")
        continue

    # ---------------- STEP 3 ----------------
    pos3 = find_target(TARGET3, CONFIDENCE)

    if pos3:
        pyautogui.click(pos3)
        print("target3 found and clicked:", pos3)
        print("Restarting session...\n")
        continue

    print("target3 not found -> going to step 4")

    if not running:
        continue

    # ==================================================
    # CAUTION3 PRIORITY BEFORE STEP4
    # ==================================================
    if find_target(CAUTION3, CONFIDENCE):
        print("CAUTION3 detected before step4! Clicking target4.")
        click_target4("(due to CAUTION3)")
        continue

    # ---------------- STEP 4 ----------------
    pos4 = find_target(TARGET4, CONFIDENCE)

    if pos4:
        caution = find_target(CAUTION1, CONFIDENCE)

        if caution:
            print("CAUTION1 detected! Skipping target4 click.")
            print("Waiting...\n")
            smart_sleep(WAIT_IF_FAIL)
            continue

        pyautogui.click(pos4)
        print("target4 found and clicked:", pos4)
        print("Restarting session...\n")
        continue

    # ---------------- FAIL CASE ----------------
    print("target4 not found. Waiting...\n")
    smart_sleep(WAIT_IF_FAIL)