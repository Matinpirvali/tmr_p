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

profile_btn = tk.CTkButton(frame_panel, text="Profile", command=profile_panel)
profile_btn.pack(anchor='ne')

# BOT assets

# Bot icon

bot_image = tk.CTkImage(dark_image=Image.open("./assets/img/icons8-bot-96.png"),size=(30, 30))

button = tk.CTkLabel(frame_panel, image=bot_image, text='')
button.pack(anchor='w',side='left')

bot_message = tk.CTkLabel(frame_panel,text='Hello')
bot_message.pack(anchor='w', side='left')



# User assets

# نمایش پنجره
window.mainloop()
