import cv2
import numpy as np
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

img = cv2.imread(file)

if img is None:
    print("Image not found")
else:
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = np.float32(gray)

    corners = cv2.cornerHarris(gray, 2, 3, 0.04)

    img[corners > 0.01 * corners.max()] = [0, 0, 255]

    cv2.imwrite(
        r"C:\Users\Admin\Desktop\harris_corners.jpg",
        img
    )

    cv2.imshow("Harris Corner Detection", img)

    print("Harris Corner Detection completed successfully")
    print("Saved on Desktop as harris_corners.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
