import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

if file_path:
    img = cv2.imread(file_path)

    if img is None:
        print("Image could not be read")
    else:
        # Convert original image to grayscale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # Histogram Equalization
        equalized = cv2.equalizeHist(gray)

        # Save output
        cv2.imwrite("equalized_image.jpg", equalized)

        # Display original and equalized images
        cv2.imshow("Original Image", gray)
        cv2.imshow("Histogram Equalized Image", equalized)

        print("Image opened successfully")
        print("Histogram Equalization applied successfully")
        print("Output saved as equalized_image.jpg")

        cv2.waitKey(0)
        cv2.destroyAllWindows()
else:
    print("No image selected")
