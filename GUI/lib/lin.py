# BDadmehr0 - Garfox
try:
    import platform
    import requests

    from tkinter import ttk
    from tkinter import *
    from customtkinter import *
    from datetime import datetime

    # from lib import sound_ef
    
except ModuleNotFoundError:
    print('App need Python3\nPelease install requirements : with "pip install -r GUI/lib/requirements.txt"\n')

def run_l():

    # APP Theme
    set_default_color_theme("dark-blue")

    home = CTk()
    home.geometry('500x600')
    home.title('TMR_P')

    setting_panel = CTkFrame(home)
    setting_panel.pack(side=RIGHT)

    bu = CTkButton(setting_panel, text='About')
    bu.pack(side=TOP)

    bot_panel = CTkFrame(home)
    bot_panel.pack()

    user_panel = CTkFrame(home)
    user_panel.pack()



    home.mainloop()

    # def log():
        # def simulate_loading():
        #     # check network connection
        #     url = 'http://www.google.com/'
        #     timeout = 5
        #     status = ''

        #     try:
        #         _ = requests.head(url, timeout=timeout)
        #         status += 'Online'
        #     except requests.ConnectionError:
        #         status += 'Offline'
        #         print("No internet connection available.")
        #         return False

        #     # Get ip public
        #     ip = requests.get('https://api.ipify.org').text

        #     # Time & platform
        #     time_log = str(datetime.now())
        #     platform_log = str(platform.platform())
        #     path = 'log/log.json'

        #     furme = '{\n    "time": "'+time_log+'",\n    "system": "' + platform_log+'",\n    "IP": "'+ip+'",\n    "status": "'+status+'"\n}\n'

        #     # Save log
        #     log = open(path, 'w')
        #     log.write(furme)
        #     log.close()
        
        # simulate_loading()

    # log()

run_l()