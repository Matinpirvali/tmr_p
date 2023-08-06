import cv2
import tkinter as tk
from tkinter import simpledialog
import requests
import numpy as np
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, root):
        self.root = root
        self.root.title("Video Player")
        
        self.video_frame = tk.Frame(root)
        self.video_frame.pack(pady=10)
        
        self.play_button = tk.Button(root, text="Play", command=self.play_video)
        self.play_button.pack(pady=5)
        
        self.pause_button = tk.Button(root, text="Pause", command=self.pause_video)
        self.pause_button.pack(pady=5)
        
        self.volume_scale = tk.Scale(root, from_=0, to=1, resolution=0.1, orient=tk.HORIZONTAL, label="Volume", command=self.set_volume)
        self.volume_scale.pack(pady=5)
        
        self.video_url = simpledialog.askstring("Video URL", "Enter video URL")
        self.cap = cv2.VideoCapture(self.video_url)

        self.play = False  # Initialize the play attribute
        
        self.update()

    def play_video(self):
        self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
        self.play = True

    def pause_video(self):
        self.play = False

    def set_volume(self, volume):
        self.cap.set(cv2.CAP_PROP_VOLUME, float(volume))

    def update(self):
        if self.play:
            ret, frame = self.cap.read()
            if ret:
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                frame_pil = Image.fromarray(frame_rgb)
                frame_tk = ImageTk.PhotoImage(image=frame_pil)
                self.video_label.config(image=frame_tk)
                self.video_label.image = frame_tk
                self.root.after(30, self.update)
            else:
                self.play = False
        else:
            self.root.after(30, self.update)

    def run(self):
        self.video_label = tk.Label(self.video_frame)
        self.video_label.pack()
        self.root.mainloop()
        self.cap.release()

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    player.run()
