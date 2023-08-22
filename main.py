import cv2
import threading
import tkinter as tk
from PIL import Image, ImageTk
import requests
import numpy as np

class VideoPlayer:
    def __init__(self, root, video_url):
        self.root = root
        self.root.title("Video Player")

        self.video_url = video_url
        self.cap = cv2.VideoCapture(self.video_url)
        self.target_width = 640  # Set your desired width
        self.target_height = 480  # Set your desired height

        self.canvas = tk.Canvas(root, width=self.target_width, height=self.target_height)
        self.canvas.pack()

        self.play_button = tk.Button(root, text="Play", command=self.play)
        self.pause_button = tk.Button(root, text="Pause", command=self.pause)

        self.play_button.pack()
        self.pause_button.pack()

        self.is_playing = False
        self.current_frame = None
        self.play_thread = None

    def play(self):
        self.is_playing = True
        self.play_button.config(state=tk.DISABLED)
        self.pause_button.config(state=tk.NORMAL)
        self.play_thread = threading.Thread(target=self._play_video)
        self.play_thread.start()

    def pause(self):
        self.is_playing = False
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

    def _play_video(self):
        while self.is_playing:
            ret, frame = self.cap.read()
            if not ret:
                self.is_playing = False
                break

            resized_frame = cv2.resize(frame, (self.target_width, self.target_height))
            self.current_frame = cv2.cvtColor(resized_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(self.current_frame)
            img = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=img)
            self.canvas.image = img
            self.root.update()

        self.cap.release()
        self.play_button.config(state=tk.NORMAL)
        self.pause_button.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    video_url = "https://upload.wikimedia.org/wikipedia/commons/transcoded/a/a7/How_to_make_video.webm/How_to_make_video.webm.720p.vp9.webm"
    player = VideoPlayer(root, video_url)
    root.mainloop()
