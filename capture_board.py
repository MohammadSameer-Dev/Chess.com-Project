# Step 1: Capture Chess.com board region

import pyautogui
import time
from PIL import Image

print("🖱️ Move your mouse to the **TOP-LEFT** corner of the board in 5 seconds...")
time.sleep(5)
top_left = pyautogui.position()
print(f"✅ Top-left corner: {top_left}")

print("🖱️ Now move your mouse to the **BOTTOM-RIGHT** corner in 5 seconds...")
time.sleep(5)
bottom_right = pyautogui.position()
print(f"✅ Bottom-right corner: {bottom_right}")

# Calculate dimensions
x1, y1 = top_left
x2, y2 = bottom_right
width = x2 - x1
height = y2 - y1

# Take screenshot
screenshot = pyautogui.screenshot(region=(x1, y1, width, height))
screenshot.save("board_capture.png")
print("📸 Board captured and saved as 'board_capture.png'")
