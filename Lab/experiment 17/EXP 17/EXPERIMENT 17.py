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
    watermark = "WATERMARK"

    cv2.putText(
        img, watermark, (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1, (0, 0, 255), 2
    )

    output_path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "watermarked_image.jpg"
    )

    cv2.imwrite(output_path, img)

    cv2.imshow("Watermarked Image", img)

    print("Watermark added successfully")
    print("Output saved as watermarked_image.jpg")

    cv2.waitKey(0)
    cv2.destroyAllWindows()
