# Step 2: Divide board into 64 squares
import cv2
import os

# Load image
image = cv2.imread("board_capture.png")
height, width = image.shape[:2]

# Dynamically calculate square width/height
square_width = width // 8
square_height = height // 8

# Output folder
output_folder = "board_squares"
os.makedirs(output_folder, exist_ok=True)

# Loop through 8x8 grid
for row in range(8):
    for col in range(8):
        x1 = col * square_width
        y1 = row * square_height
        x2 = x1 + square_width
        y2 = y1 + square_height

        square = image[y1:y2, x1:x2]

        # File and rank mapping (a-h, 8-1)
        file = chr(ord('a') + col)
        rank = str(8 - row)
        filename = f"{file}{rank}.png"

        cv2.imwrite(os.path.join(output_folder, filename), square)

print("✅ Squares saved correctly to 'board_squares/' folder.")
