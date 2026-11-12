import cv2
from tkinter import Tk, filedialog

# Select image
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.jpeg *.png")]
)

if not path:
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

# Count and mark faces
count = len(faces)

for (x, y, w, h) in faces:
    cv2.rectangle(
        img, (x, y), (x+w, y+h), (0, 255, 0), 2
    )

# Display face count
print("Number of faces detected:", count)

cv2.putText(
    img,
    "Faces: " + str(count),
    (20, 40),
    cv2.FONT_HERSHEY_SIMPLEX,
    1,
    (0, 0, 255),
    2
)

# Display result
cv2.imshow("Face Counting", img)

# Save output
cv2.imwrite(
    "C:/Users/Admin/Desktop/face_count.jpg", img
)

cv2.waitKey(0)
cv2.destroyAllWindows()
