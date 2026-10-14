import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file = filedialog.askopenfilename()

img = cv2.imread(file)

if img is None:
    print("Image not found")
else:
    rotated = cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

    cv2.imwrite(r"C:\Users\Admin\Desktop\rotated_image.jpg", rotated)

    cv2.imshow("Original Image", img)
    cv2.imshow("Rotated Image", rotated)

    print("90-degree clockwise rotation completed")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
