import cv2
import numpy as np

def create_circle(height, width):

    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Calculate center and radius
    center = (width // 2, height // 2)
    radius = min(height, width) // 4

    # Draw circle
    cv2.circle(img, center, radius, (0, 0, 255), 3)

    return img

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

result = create_circle(height, width)

cv2.imshow("Circle Shape", result)

cv2.imwrite(
    "C:/Users/Admin/Desktop/circle.jpg",
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Circle created successfully!")
