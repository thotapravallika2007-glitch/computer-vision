import cv2
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

# Get text from user
text = input("Enter the text: ")

# Add text to image
cv2.putText(
    img,
    text,
    (50, 100),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

# Display image
cv2.imshow("Text on Image", img)

# Save output
cv2.imwrite(
    "C:/Users/Admin/Desktop/text_image.jpg",
    img
)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Text added successfully!")
