import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file = filedialog.askopenfilename()

img = cv2.imread(file)

if img is None:
    print("Image not found")
else:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

    dilated = cv2.dilate(img, kernel)

    cv2.imwrite(r"C:\Users\Admin\Desktop\dilated_image.jpg", dilated)

    cv2.imshow("Original Image", img)
    cv2.imshow("Dilated Image", dilated)

    print("Image dilation completed successfully")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
