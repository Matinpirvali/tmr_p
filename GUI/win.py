import platform
import subprocess
import requests
import time
import os

from tkinter import *
from customtkinter import *
from datetime import datetime

# APP Theme
set_default_color_theme("dark-blue") 

def log():
    def task():
        # The window will stay open until this function call ends.
        time.sleep(2)
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
        path = 'data/log.json'

        furme = '{\n    "time": "'+time_log+'",\n    "system": "' + platform_log+'",\n    "IP": "'+ip+'",\n    "status": "'+status+'"\n}\n'

        # Save log
        log = open(path, 'w')
        log.write(furme)
        log.close()
        root.destroy()

    # Load page tk
    root = CTk()
    root.title("Loading")
    root.resizable(False, False)  # تغییر اندازه پنجره غیرفعال شود

    label = Label(root, text="Waiting for task to finish.")
    label.pack()

    root.after(200, task)
    root.mainloop()

def main_bot():
    root = CTk()
    root.title('TMR_P')
    root.geometry('300x200')  # تنظیم اندازه پنجره

    root.mainloop()

if __name__ == "__main__":
    log()
    main_bot()
