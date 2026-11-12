import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

path = filedialog.askopenfilename(
    filetypes=[("Images", "*.jpg *.jpeg *.png")]
)

if not path:
    exit()

img = cv2.imread(path)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

face = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)

eye = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_eye.xml"
)

faces = face.detectMultiScale(gray, 1.3, 5)

for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

    eyes = eye.detectMultiScale(roi_gray)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(
            roi_color,
            (ex, ey),
            (ex+ew, ey+eh),
            (0, 255, 0), 2
        )

cv2.imshow("Eye Detection", img)

cv2.imwrite(
    "C:/Users/Admin/Desktop/eye_detected.jpg", img
)

cv2.waitKey(0)
cv2.destroyAllWindows()
