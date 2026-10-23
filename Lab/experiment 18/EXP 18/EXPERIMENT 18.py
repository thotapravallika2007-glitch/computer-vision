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
    roi = img[50:200, 50:200]
    copied = roi.copy()

    img[220:370, 220:370] = copied

    folder = os.path.dirname(os.path.abspath(__file__))

    cv2.imwrite(os.path.join(folder, "cropped_image.jpg"), roi)
    cv2.imwrite(os.path.join(folder, "roi_output.jpg"), img)

    cv2.imshow("Cropped ROI", roi)
    cv2.imshow("Image After Pasting ROI", img)

    print("Cropping, copying and pasting completed")
    print("Output images saved successfully")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
