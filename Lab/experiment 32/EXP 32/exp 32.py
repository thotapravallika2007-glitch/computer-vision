import cv2
import numpy as np

def create_image(height, width):

    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate box size
    h = height // 10
    w = width // 10

    # Create colored boxes at four corners
    img[0:h, 0:w] = [0, 0, 0]           # Black
    img[0:h, width-w:width] = [255, 0, 0]  # Blue
    img[height-h:height, 0:w] = [0, 255, 0]  # Green
    img[height-h:height, width-w:width] = [0, 0, 255]  # Red

    return img

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

result = create_image(height, width)

cv2.imshow("White Image with Colored Boxes", result)

cv2.imwrite("C:/Users/Admin/Desktop/colored_boxes.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image created successfully!")
