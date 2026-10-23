import cv2
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
    kernel = cv2.getStructuringElement(
        cv2.MORPH_RECT, (5, 5)
    )

    closed = cv2.morphologyEx(
        img, cv2.MORPH_CLOSE, kernel
    )

    folder = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(folder, "closed_image.jpg")

    cv2.imwrite(output_path, closed)

    cv2.imshow("Original Image", img)
    cv2.imshow("Closing Operation", closed)

    print("Closing operation completed successfully")
    print("Output saved as closed_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
