import cv2
import matplotlib.pyplot as plt
from tkinter import Tk, filedialog

root = Tk()
root.withdraw()

file = filedialog.askopenfilename()

img = cv2.imread(file)

if img is None:
    print("Image not found")
else:
    colors = ('b', 'g', 'r')

    for i, color in enumerate(colors):
        hist = cv2.calcHist([img], [i], None, [256], [0, 256])
        plt.plot(hist, color=color)

    plt.title("Color Histogram")
    plt.xlabel("Color Levels")
    plt.ylabel("Pixel Count")
    plt.show()

    print("Color histogram completed successfully")
