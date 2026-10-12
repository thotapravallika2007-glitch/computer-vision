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
    rows, cols = img.shape[:2]

    pts1 = np.float32([
        [50, 50],
        [200, 50],
        [50, 200]
    ])

    pts2 = np.float32([
        [10, 100],
        [200, 50],
        [100, 250]
    ])

    matrix = cv2.getAffineTransform(pts1, pts2)

    transformed = cv2.warpAffine(img, matrix, (cols, rows))

    cv2.imwrite(
        r"C:\Users\Admin\Desktop\affine_transformed.jpg",
        transformed
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("Affine Transformed Image", transformed)

    print("Affine transformation completed successfully")
    print("Saved on Desktop as affine_transformed.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
