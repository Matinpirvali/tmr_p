import customtkinter as ctk

# Video List
video_list = [
    "Video 1",
    "Video 2",
    "Video 3",
    "Video 4"
]

def play_video(video_name):
    # Video Player
    print(f"Playing Video: {video_name}")

def search_videos():
    keyword = search_entry.get()

    # Delet Before Button
    for button in video_buttons:
        button.destroy()
    
    for video in video_list:
        if keyword.lower() in video.lower():
            # Create new Buttons for Videos
            video_button = ctk.CTkButton(root, text=video, command=lambda v=video: play_video(v))
            video_button.grid(row=video_list.index(video)+2, column=0, padx=10, pady=5)
            video_buttons.append(video_button)

root = ctk.CTk()

search_label = ctk.CTkLabel(root, text="Search:")
search_label.grid(row=0, column=0, padx=10, pady=5)

search_entry = ctk.CTkEntry(root, width=30)
search_entry.grid(row=0, column=1, padx=10, pady=5)

search_button = ctk.CTkButton(root, text="Search", command=search_videos)
search_button.grid(row=0, column=2, padx=10, pady=5)

# List Buttons
video_buttons = []

root.mainloop()