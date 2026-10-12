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
        [cols - 50, 50],
        [50, rows - 50],
        [cols - 50, rows - 50]
    ])

    pts2 = np.float32([
        [0, 0],
        [cols, 50],
        [50, rows],
        [cols - 50, rows - 20]
    ])

    matrix = cv2.getPerspectiveTransform(pts1, pts2)

    transformed = cv2.warpPerspective(
        img, matrix, (cols, rows)
    )

    cv2.imwrite(
        r"C:\Users\Admin\Desktop\perspective_transformed.jpg",
        transformed
    )

    cv2.imshow("Original Image", img)
    cv2.imshow("Perspective Transformed Image", transformed)

    print("Perspective transformation completed successfully")
    print("Saved on Desktop as perspective_transformed.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
