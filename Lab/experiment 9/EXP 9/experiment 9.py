import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file = filedialog.askopenfilename()

img = cv2.imread(file)

if img is None:
    print("Image not found")
else:
    big = cv2.resize(img, None, fx=2, fy=2)
    small = cv2.resize(img, None, fx=0.5, fy=0.5)

    cv2.imwrite(r"C:\Users\Admin\Desktop\big_image.jpg", big)
    cv2.imwrite(r"C:\Users\Admin\Desktop\small_image.jpg", small)

    cv2.imshow("Original Image", img)
    cv2.imshow("Bigger Image", big)
    cv2.imshow("Smaller Image", small)

    print("Image scaling completed successfully")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
