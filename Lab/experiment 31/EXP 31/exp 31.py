import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.jpeg *.png")]
)

if not path:
    exit()

img = cv2.imread(path)

if img is None:
    print("Unable to read image")
    exit()

# Convert image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Set threshold values
lower = 100
upper = 200

# Apply threshold segmentation
_, segmented = cv2.threshold(
    gray, lower, upper, cv2.THRESH_BINARY
)

# Display original and segmented images
cv2.imshow("Original Image", img)
cv2.imshow("Segmented Image", segmented)

# Save segmented image
cv2.imwrite(
    "C:/Users/Admin/Desktop/segmented_image.jpg",
    segmented
)

cv2.waitKey(0)
cv2.destroyAllWindows()
