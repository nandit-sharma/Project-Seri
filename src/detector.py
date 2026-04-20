# import pyautogui
# from pyautogui import ImageNotFoundException

# pyautogui.FAILSAFE = False

# def find_target(image_path, confidence=0.8):
#     try:
#         location = pyautogui.locateOnScreen(image_path, confidence=confidence)
#         if location:
#             return pyautogui.center(location)
#         return None

#     except ImageNotFoundException:
#         return None   # ✅ just return None silently

#     except Exception as e:
#         print("Detection error:", e)
#         return None









import pyautogui

def find_target(image_path, confidence=0.8):
    try:
        location = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if location:
            return pyautogui.center(location)
        return None
    except pyautogui.ImageNotFoundException:
        return None