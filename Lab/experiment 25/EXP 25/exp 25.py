import cv2
from ultralytics import YOLO
from tkinter import Tk, filedialog

# Select image
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Watch Image",
    filetypes=[("Images", "*.jpg *.jpeg *.png")]
)

if not path:
    exit()

# Load YOLO model
model = YOLO("yolov8s-world.pt")

# Set watch as target object
model.set_classes(["watch"])

# Read image
img = cv2.imread(path)

if img is None:
    print("Unable to read image")
    exit()

# Detect watch
results = model.predict(img, conf=0.20)

# Draw detection box
output = results[0].plot()

# Display result
cv2.imshow("Watch Recognition", output)

# Save output
cv2.imwrite(
    "C:/Users/Admin/Desktop/watch_detected.jpg",
    output
)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Watch recognition completed!")
