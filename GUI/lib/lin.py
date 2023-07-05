from PIL import Image
import customtkinter as tk

def about_panel():
    print("Button clicked!")

def profile_panel():
    print('profile')

# Main Seeting up
window = tk.CTk()
window.geometry('550x600')


# Other assets
frame_panel = tk.CTkFrame(window)
frame_panel.pack(side='top', anchor='n', fill='x')

# About button
about_btn = tk.CTkButton(frame_panel, text="About", command=about_panel)
about_btn.pack(anchor='ne')

about_btn = tk.CTkButton(frame_panel, text="Profile", command=profile_panel)
about_btn.pack(anchor='ne')

bot_message = tk.CTkLabel(frame_panel,text='Hello')
bot_message.pack(anchor='w')

# Bot icon

my_image = tk.CTkImage(dark_image=Image.open("<path to dark mode image>"),size=(30, 30))

button = tk.CTkButton(frame_panel, image=my_image)


# User assets

# نمایش پنجره
window.mainloop()
