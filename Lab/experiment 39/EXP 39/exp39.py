import cv2
from tkinter import Tk, filedialog

# Select video
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)

if not path:
    exit()

cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Unable to open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

if fps <= 0:
    fps = 25

frames = []

while True:
    ret, frame = cap.read()
    if not ret:
        break
    frames.append(frame)

cap.release()

# Create output video on Desktop
out = cv2.VideoWriter(
    "C:/Users/Admin/Desktop/reverse_slow_motion.mp4",
    cv2.VideoWriter_fourcc(*'mp4v'),
    fps / 2,
    (width, height)
)

# Save frames in reverse order
for frame in reversed(frames):
    out.write(frame)

    cv2.imshow("Reverse Slow Motion", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

out.release()
cv2.destroyAllWindows()

print("Video saved successfully on Desktop!")
