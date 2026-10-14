import cv2
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file = filedialog.askopenfilename(
    title="Select Video",
    filetypes=[("Video Files", "*.mp4 *.avi *.mov")]
)

cap = cv2.VideoCapture(file)

if not cap.isOpened():
    print("Video not found")
else:
    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0:
        fps = 30

    frames = []

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        frames.append(cv2.resize(frame, (320, 240)))

    cap.release()

    out = cv2.VideoWriter(
        r"C:\Users\Admin\Desktop\three_speed_video.mp4",
        cv2.VideoWriter_fourcc(*"mp4v"),
        fps,
        (960, 240)
    )

    i = 0

    while i < len(frames):
        normal = frames[i]

        slow = frames[i // 2]

        fast = frames[min(i * 2, len(frames) - 1)]

        cv2.putText(normal, "NORMAL", (90, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

        cv2.putText(slow, "SLOW", (110, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

        cv2.putText(fast, "FAST", (110, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255,255,255), 2)

        result = cv2.hconcat([normal, slow, fast])

        out.write(result)
        cv2.imshow("Normal | Slow | Fast", result)

        if cv2.waitKey(30) & 0xFF == ord("q"):
            break

        i += 1

    out.release()
    cv2.destroyAllWindows()

    print("Completed successfully")
    print("Saved on Desktop as three_speed_video.mp4")
