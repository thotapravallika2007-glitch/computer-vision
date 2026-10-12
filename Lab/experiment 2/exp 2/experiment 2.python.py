from PIL import Image, ImageFilter
from tkinter import Tk, filedialog
import os

root = Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select your image",
    filetypes=[("Image files", "*.jpg *.jpeg *.png")]
)

if file_path:
    img = Image.open(file_path)

    print("Image opened successfully")
    print("Image size:", img.size)

    blur = img.filter(ImageFilter.GaussianBlur(5))

    folder = os.path.dirname(file_path)
    output = os.path.join(folder, "blur_photo.jpg")

    blur.save(output)

    print("Gaussian Blur applied successfully")
    print("Output saved as:", output)
else:
    print("No image selected")
