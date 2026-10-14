import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select an Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

if file_path:
    img = cv2.imread(file_path)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edges = cv2.Canny(gray, 100, 200)

    cv2.imwrite("canny_output.jpg", edges)

    print("Image opened successfully")
    print("Canny edge detection applied successfully")
    print("Output saved as canny_output.jpg")

    cv2.imshow("Canny Edge Output", edges)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("No image selected")
