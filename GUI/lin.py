# BDadmehr0 - Garfox
try:
    import platform
    import subprocess
    import requests
    import time
    import os

    from tkinter import ttk
    from tkinter import *
    from customtkinter import *
    from datetime import datetime
    # from lib import sound_ef
except ModuleNotFoundError:
   print('App need Python3\nPelease install requirements : with "pip install -r GUI/lib/requirements.txt"\n')

# APP Theme
set_default_color_theme("dark-blue")


def main_bot():
    def button_send_main():

        def button_send_task():
            pass
        
        if n == 1:
            button_send_main()

    home = CTk()
    home.title('TMR_P')
    home.geometry('600x600')
    
    # BOT Aseets
    frame_bot = CTkFrame(home)
    frame_bot.pack(padx=10,pady=12)

    bot_tit_lb = CTkLabel(frame_bot, text='Bot', font=('Roboto', 25), width=600, height=100)
    bot_tit_lb.pack(side=RIGHT)

    bot_lb = CTkLabel(frame_bot, text='')
    bot_lb.pack()

    home.mainloop()

def log():
    def simulate_loading():
        progress_bar.start(10) # Start the progress bar animation
        # Simulate a loading process
        # You can replace this with your actual loading logic
        # Here, we're using a simple time delay to simulate the loading process
        # The window will stay open until this function call ends.

        # check network connection
        url = 'http://www.google.com/'
        timeout = 5
        status = ''

        try:
            _ = requests.head(url, timeout=timeout)
            status += 'Online'
        except requests.ConnectionError:
            status += 'Offline'
            print("No internet connection available.")
            return False

        # Get ip public
        ip = requests.get('https://api.ipify.org').text

        # Time & platform
        time_log = str(datetime.now())
        platform_log = str(platform.platform())
        path = 'log/log.json'

        furme = '{\n    "time": "'+time_log+'",\n    "system": "' + platform_log+'",\n    "IP": "'+ip+'",\n    "status": "'+status+'"\n}\n'

        # Save log
        log = open(path, 'w')
        log.write(furme)
        log.close()
        root.destroy()
        root.after(3000, finish_loading)

    def finish_loading():
        progress_bar.stop()  # Stop the progress bar animation
        root.destroy()  # Close the loading menu and proceed to the main application

    root = CTk()
    root.title("Loading Menu")
    root.geometry("300x100")

    # Create a frame
    frame = ttk.CTkFrame(root)
    frame.pack(pady=20)

    # Create a progress bar
    progress_bar = ttk.Progressbar(frame, orient="horizontal", mode="indeterminate")
    progress_bar.pack(pady=10)

    # Create a button to start the loading process
    start_button = ttk.Button(frame, text="Start", command=simulate_loading)
    start_button.pack()

    root.mainloop()



if __name__ == "__main__":
    main_bot()