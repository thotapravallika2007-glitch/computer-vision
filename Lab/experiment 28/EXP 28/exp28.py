import cv2
from ultralytics import YOLO
from tkinter import Tk, filedialog

# Select video
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Traffic Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)

if not path:
    print("No video selected")
    exit()

# Load YOLO model
model = YOLO("yolov8n.pt")

# Open video
cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Unable to open video")
    exit()

# Get video properties
fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 25

# Create output video
output_path = "C:/Users/Admin/Desktop/vehicle_detection_output.mp4"

fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # Detect vehicles
    results = model.predict(
        frame,
        classes=[2, 3, 5, 7],
        conf=0.25,
        verbose=False
    )

    # Draw detection boxes
    output = results[0].plot()

    # Save processed frame
    out.write(output)

    # Display result
    cv2.imshow("Vehicle Detection", output)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()

print("Processed video saved successfully!")
print(output_path)
