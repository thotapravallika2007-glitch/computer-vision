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

# Define background color levels
lower = np.array([0, 0, 180])
upper = np.array([180, 60, 255])

# Detect background
mask = cv2.inRange(hsv, lower, upper)

# Subtract background
result = cv2.bitwise_and(img, img, mask=cv2.bitwise_not(mask))

# Display images
cv2.imshow("Original Image", img)
cv2.imshow("Background Mask", mask)
cv2.imshow("Background Removed", result)

# Save output
cv2.imwrite(
    "C:/Users/Admin/Desktop/background_removed.jpg",
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Background removed successfully!")
