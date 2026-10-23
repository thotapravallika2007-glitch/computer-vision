import cv2
import numpy as np
from tkinter import Tk, filedialog
import os

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

    sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)

    x = cv2.convertScaleAbs(sobel_x)
    y = cv2.convertScaleAbs(sobel_y)

    result = cv2.addWeighted(x, 0.5, y, 0.5, 0)

    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "sobel_output.jpg"
    )

    cv2.imwrite(output_path, result)

    cv2.imshow("Original Image", img)
    cv2.imshow("Sobel Filtered Image", result)

    print("Sobel filtering completed successfully")
    print("Output saved as sobel_output.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
