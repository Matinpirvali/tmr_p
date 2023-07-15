from PIL import Image
import customtkinter as tk

def about_panel():
    print("Button clicked!")

def profile_panel():
    print('profile')

# Main Seeting up
window = tk.CTk()
window.geometry('550x600')
# window.iconbitmap('/home/dadmehremami/Documents/GitHub/tmr_p/GUI/lib/assets/icon.ico')

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

bot_image = tk.CTkImage(dark_image=Image.open("./assets/img/icons8-bot-96.png"),size=(50, 50))

image_lb = tk.CTkLabel(frame_panel, image=bot_image, text='')
image_lb.pack(anchor='w',side='left')

bot_message = tk.CTkLabel(frame_panel, text='Hello', font=('Arial', 20))
bot_message.pack(anchor='w', side='left')


# User assets

window.mainloop()