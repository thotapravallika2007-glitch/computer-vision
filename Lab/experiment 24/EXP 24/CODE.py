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

    result = cv2.morphologyEx(
        img, cv2.MORPH_BLACKHAT, kernel
    )

    folder = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(folder, "blackhat_image.jpg")

    cv2.imwrite(output_path, result)

    cv2.imshow("Original Image", img)
    cv2.imshow("Black-Hat Image", result)

    print("Black-Hat operation completed successfully")
    print("Output saved as blackhat_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
