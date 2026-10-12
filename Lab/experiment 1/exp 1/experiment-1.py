from PIL import Image

img = Image.open("image.jpg")

print("Image opened successfully")
print("Image size:", img.size)

gray = img.convert("L")

gray.save("gray_image.jpg")

print("Image converted to grayscale")
print("Grayscale image saved as gray_image.jpg")
