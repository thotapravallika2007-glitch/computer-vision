import cv2
import numpy as np
from tkinter import Tk, filedialog

# Select image
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.jpeg *.png")]
)

if not path:
    exit()

# Read image
img = cv2.imread(path)

if img is None:
    print("Unable to read image")
    exit()

# Convert image to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Define foreground color levels (green)
lower = np.array([35, 40, 40])
upper = np.array([85, 255, 255])

# Detect foreground
mask = cv2.inRange(hsv, lower, upper)

# Subtract foreground
result = cv2.bitwise_and(
    img, img, mask=cv2.bitwise_not(mask)
)

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Foreground Mask", mask)
cv2.imshow("Foreground Removed", result)

# Save output
cv2.imwrite(
    "C:/Users/Admin/Desktop/foreground_removed.jpg",
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Foreground subtraction completed!")
