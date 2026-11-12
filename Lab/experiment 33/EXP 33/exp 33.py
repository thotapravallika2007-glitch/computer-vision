import cv2
import numpy as np

def create_rectangle(height, width):

    # Create white image
    img = np.ones((height, width, 3), dtype=np.uint8) * 255

    # Draw rectangle
    cv2.rectangle(
        img,
        (width//4, height//4),
        (3*width//4, 3*height//4),
        (0, 0, 255),
        3
    )

    return img

height = int(input("Enter image height: "))
width = int(input("Enter image width: "))

result = create_rectangle(height, width)

cv2.imshow("Rectangle Shape", result)

cv2.imwrite(
    "C:/Users/Admin/Desktop/rectangle.jpg",
    result
)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Rectangle created successfully!")
