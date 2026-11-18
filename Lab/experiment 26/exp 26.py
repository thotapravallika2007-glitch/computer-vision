import cv2
from tkinter import Tk, filedialog

# Select input video
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Input Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)

if not path:
    exit()

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

# Read all frames
frames = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    frames.append(frame)

cap.release()

if not frames:
    print("No frames found")
    exit()

print("Total frames:", len(frames))

# Create output video
output_path = "C:/Users/Admin/Desktop/reverse_video.mp4"

out = cv2.VideoWriter(
    output_path,
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps,
    (width, height)
)

if not out.isOpened():
    print("Unable to create output video")
    exit()

# Write frames in reverse order
for frame in reversed(frames):
    out.write(frame)

    cv2.imshow("Reverse Video", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        print("Preview stopped. Output video is still being saved.")
        break

out.release()
cv2.destroyAllWindows()

print("Reverse video created successfully!")
print("Output:", output_path)
