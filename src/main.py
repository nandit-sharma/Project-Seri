# import time
# import pyautogui
# import keyboard
# from plyer import notification
# from detector import find_target

# TARGET1 = "assets/target1.png"
# TARGET2 = "assets/target2.png"
# TARGET3 = "assets/target3.png"
# TARGET4 = "assets/target4.png"
# CAUTION1 = "assets/caution1.png"

# CONFIDENCE = 0.8
# START_DELAY = 5
# WAIT_IF_FAIL = 180  # 5 seconds

# running = False


# def show_notification(title, message):
#     notification.notify(
#         title=title,
#         message=message,
#         timeout=3
#     )


# def toggle_bot():
#     global running
#     running = not running

#     if running:
#         print("\nBOT STARTED\n")
#         show_notification("AutoClick Bot", "BOT STARTED")
#     else:
#         print("\nBOT STOPPED\n")
#         show_notification("AutoClick Bot", "BOT STOPPED")


# keyboard.add_hotkey("ctrl+shift+alt+s", toggle_bot)

# print("Program started.")
# print("Press Ctrl+Shift+Alt+S to START/STOP bot.\n")


# while True:

#     # bot OFF mode
#     if not running:
#         time.sleep(0.2)
#         continue

#     # ---------------- STEP 1 ----------------
#     print("Session started... waiting 5 seconds")
#     time.sleep(START_DELAY)

#     if not running:
#         continue

#     pos1 = find_target(TARGET1, CONFIDENCE)

#     if pos1:
#         pyautogui.click(pos1)
#         print("target1 found and clicked:", pos1)
#         # continue to step 2
#     else:
#         print("target1 not found -> going to step 2")

#     if not running:
#         continue

#     # ---------------- STEP 2 ----------------
#     pos2 = find_target(TARGET2, CONFIDENCE)

#     if pos2:
#         pyautogui.click(pos2)
#         print("target2 found and clicked:", pos2)
#         print("Restarting session...\n")
#         continue

#     print("target2 not found. Moving mouse to center...")

#     # move mouse to center
#     w, h = pyautogui.size()
#     pyautogui.moveTo(w // 2, h // 2)

#     if not running:
#         continue

#     # find target2 again
#     pos2 = find_target(TARGET2, CONFIDENCE)

#     if pos2:
#         pyautogui.click(pos2)
#         print("target2 found after moving mouse. Clicked:", pos2)
#         print("Restarting session...\n")
#         continue

#     print("target2 still not found -> going to step 3")

#     if not running:
#         continue

#     # ---------------- STEP 3 ----------------
#     pos3 = find_target(TARGET3, CONFIDENCE)

#     if pos3:
#         pyautogui.click(pos3)
#         print("target3 found and clicked:", pos3)
#         print("Restarting session...\n")
#         continue

#     print("target3 not found -> going to step 4")

#     if not running:
#         continue

#     # ---------------- STEP 4 ----------------
#     pos4 = find_target(TARGET4, CONFIDENCE)

#     if pos4:
#         pyautogui.click(pos4)
#         print("target4 found and clicked:", pos4)
#         print("Restarting session...\n")
#         continue

#     # ---------------- FAIL CASE ----------------
#     print("target4 not found. Waiting 5 seconds...\n")

#     for _ in range(WAIT_IF_FAIL):
#         if not running:
#             break
#         time.sleep(1)

















import time
import pyautogui
import keyboard
from plyer import notification
from detector import find_target

TARGET1 = "assets/target1.png"
TARGET2 = "assets/target2.png"
TARGET3 = "assets/target3.png"
TARGET4 = "assets/target4.png"
CAUTION1 = "assets/caution1.png"

CONFIDENCE = 0.8
START_DELAY = 5
WAIT_IF_FAIL = 5

running = False


def show_notification(title, message):
    notification.notify(
        title=title,
        message=message,
        timeout=3
    )


def toggle_bot():
    global running
    running = not running

    if running:
        print("\nBOT STARTED\n")
        show_notification("AutoClick Bot", "BOT STARTED")
    else:
        print("\nBOT STOPPED\n")
        show_notification("AutoClick Bot", "BOT STOPPED")


keyboard.add_hotkey("ctrl+shift+alt+s", toggle_bot)

print("Program started.")
print("Press Ctrl+Shift+Alt+S to START/STOP bot.\n")


while True:

    # bot OFF mode
    if not running:
        time.sleep(0.2)
        continue

    # ---------------- STEP 1 ----------------
    print("Session started... waiting 5 seconds")
    time.sleep(START_DELAY)

    if not running:
        continue

    pos1 = find_target(TARGET1, CONFIDENCE)

    if pos1:
        pyautogui.click(pos1)
        print("target1 found and clicked:", pos1)
        # continue to step 2
    else:
        print("target1 not found -> going to step 2")

    if not running:
        continue

    # ---------------- STEP 2 ----------------
    pos2 = find_target(TARGET2, CONFIDENCE)

    if pos2:
        pyautogui.click(pos2)
        print("target2 found and clicked:", pos2)
        print("Restarting session...\n")
        continue

    print("target2 not found. Moving mouse to center...")

    # move mouse to center
    w, h = pyautogui.size()
    pyautogui.moveTo(w // 2, h // 2)
    pyautogui.moveTo(w // 2, (h // 2) - 40)

    if not running:
        continue

    # find target2 again
    pos2 = find_target(TARGET2, CONFIDENCE)

    if pos2:
        pyautogui.click(pos2)
        print("target2 found after moving mouse. Clicked:", pos2)
        print("Restarting session...\n")
        continue

    print("target2 still not found -> going to step 3")

    if not running:
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

    # ---------------- STEP 4 ----------------
    pos4 = find_target(TARGET4, CONFIDENCE)

    if pos4:
        caution = find_target(CAUTION1, CONFIDENCE)

        if caution:
            print("CAUTION detected! Skipping target4 click.")
            print("Waiting 5 seconds...\n")

            for _ in range(WAIT_IF_FAIL):
                if not running:
                    break
                time.sleep(1)

            continue

        pyautogui.click(pos4)
        print("target4 found and clicked:", pos4)
        print("Restarting session...\n")
        continue

    # ---------------- FAIL CASE ----------------
    print("target4 not found. Waiting 5 seconds...\n")

    for _ in range(WAIT_IF_FAIL):
        if not running:
            break
        time.sleep(1)