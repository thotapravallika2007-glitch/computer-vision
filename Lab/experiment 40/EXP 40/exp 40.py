import cv2
import pytesseract
from tkinter import Tk, filedialog

# Set Tesseract path
pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)

# Select video
root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    title="Select Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)

if not path:
    exit()

# Open video
cap = cv2.VideoCapture(path)

if not cap.isOpened():
    print("Unable to open video")
    exit()

fps = cap.get(cv2.CAP_PROP_FPS)

if fps <= 0:
    fps = 25

interval = max(1, int(fps))
frame_count = 0
all_text = []

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if frame_count % interval == 0:

        # Convert frame to grayscale
        gray = cv2.cvtColor(
            frame, cv2.COLOR_BGR2GRAY
        )

        # Extract text
        text = pytesseract.image_to_string(gray)

        if text.strip():
            all_text.append(text.strip())

        print("Processing frame:", frame_count)

    frame_count += 1

cap.release()

# Save extracted text
output_path = "C:/Users/Admin/Desktop/extracted_text.txt"

with open(output_path, "w", encoding="utf-8") as file:
    file.write("\n".join(all_text))

print("Text extracted successfully!")
print("Output saved at:", output_path)
