from PIL import Image
import customtkinter as tk

def run_l():

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
    about_btn = tk.CTkButton(frame_panel, text="About", command=about_panel, width=100, font=('bold', 15))
    about_btn.pack(padx=12, pady=5, anchor='ne')

    profile_btn = tk.CTkButton(frame_panel, text="Profile", command=profile_panel, width=100, font=('bold', 15))
    profile_btn.pack(padx=12, pady=1, anchor='ne')

    # BOT assets

    # Bot icon

    bot_image = tk.CTkImage(dark_image=Image.open("./assets/img/icons8-bot-96.png"),size=(50, 50))

    image_lb = tk.CTkLabel(frame_panel, image=bot_image, text='')
    image_lb.pack(padx=12, pady=1, anchor='w',side='left')

    bot_message = tk.CTkLabel(frame_panel, text='Hello', font=('Arial', 20))
    bot_message.pack(anchor='w', side='left')


    # User assets

    user_frame = tk.CTkFrame(window)
    user_frame.pack(padx=12, pady=10, anchor='s', fill='x', side='bottom')

    user_i = tk.CTkEntry(user_frame, width=375, font=('Roboto', 17))
    user_i.pack(padx=12, pady=10, side='left')

    
    user_send_btn_img = tk.CTkImage(dark_image=Image.open("./assets/img/send.png") , size=(30, 30))

    user_send_btn = tk.CTkButton(user_frame, image=user_send_btn_img, text='', corner_radius=100, width=100, font=('bold', 15))
    user_send_btn.pack(padx=12, pady=10, side='right')

    window.mainloop()