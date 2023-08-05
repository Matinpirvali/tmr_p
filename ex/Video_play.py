import tkinter as tk
from tkinter import ttk

# مثالی از یک لیست ویدیوها
video_list = [
    "ویدیو 1",
    "ویدیو 2",
    "ویدیو 3",
    "ویدیو 4",
    "ویدیو 5",
]

def play_video(video_name):
    # تابعی که وقتی دکمه‌ی ویدیو فشرده می‌شود، فراخوانی می‌شود
    # اینجا می‌توانید از کتابخانه‌ی ویدئو پلیر استفاده کنید
    # اینجا نمونه‌ای از پیغامی که نشان دهد کدام ویدیو فشرده شده است، آورده‌ایم.
    print(f"در حال پخش ویدیو: {video_name}")

def search_videos():
    # این تابع به عنوان callback برای دکمه‌ی جستجو فراخوانی می‌شود
    keyword = search_entry.get()  # متن وارد شده در جستجو را می‌گیریم
    # حذف دکمه‌های قبلی (اگر وجود داشته باشند)
    for button in video_buttons:
        button.destroy()
    for video in video_list:
        if keyword.lower() in video.lower():
            # ایجاد دکمه‌ی جدید برای هر ویدیو
            video_button = ttk.Button(root, text=video, command=lambda v=video: play_video(v))
            video_button.grid(row=video_list.index(video)+2, column=0, padx=10, pady=5)
            video_buttons.append(video_button)

# ایجاد پنجره اصلی
root = tk.Tk()
root.title("جستجو ویدیو")

# ایجاد ویجت‌ها
search_label = ttk.Label(root, text="جستجو:")
search_label.grid(row=0, column=0, padx=10, pady=5)

search_entry = ttk.Entry(root, width=30)
search_entry.grid(row=0, column=1, padx=10, pady=5)

search_button = ttk.Button(root, text="جستجو", command=search_videos)
search_button.grid(row=0, column=2, padx=10, pady=5)

# لیستی برای نگهداری دکمه‌ها
video_buttons = []

# اجرای برنامه
root.mainloop()

