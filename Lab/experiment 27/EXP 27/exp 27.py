import cv2
from tkinter import Tk, filedialog

# Select image
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Image",
    filetypes=[("Image Files", "*.jpg *.jpeg *.png")]
)

if not path:
    print("No image selected")
    exit()

# Read image
img = cv2.imread(path)

if img is None:
    print("Unable to read image")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Load face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

# Detect faces
faces = face_cascade.detectMultiScale(
    gray, 1.1, 5
)

# Draw rectangles
for (x, y, w, h) in faces:
    cv2.rectangle(
        img, (x, y), (x+w, y+h), (0, 255, 0), 2
    )

print("Number of faces detected:", len(faces))

# Display result
cv2.imshow("Face Detection", img)

# Save result
cv2.imwrite(
    "C:/Users/Admin/Desktop/face_detected.jpg", img
)

cv2.waitKey(0)
cv2.destroyAllWindows()
