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

    dilated = cv2.dilate(img, kernel, iterations=1)

    folder = os.path.dirname(os.path.abspath(__file__))
    output_path = os.path.join(folder, "dilated_image.jpg")

    cv2.imwrite(output_path, dilated)

    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", dilated)

    print("Dilation completed successfully")
    print("Output saved as dilated_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
