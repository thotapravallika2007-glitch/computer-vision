import cv2
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
    rotated = cv2.rotate(img, cv2.ROTATE_180)

    cv2.imwrite(r"C:\Users\Admin\Desktop\rotated_180_image.jpg", rotated)

    cv2.imshow("Original Image", img)
    cv2.imshow("180 Degree Rotated Image", rotated)

    print("180-degree rotation completed successfully")
    print("Saved on Desktop as rotated_180_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
