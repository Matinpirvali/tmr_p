from tkinter import *
from time import sleep
import requests
from datetime import datetime
import platform

def task():
    # The window will stay open until this function call ends.

    sleep(2)
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

    furme = '{\n    "time": "'+time_log+'",\n    "system": "' + \
        platform_log+'",\n    "IP": "'+ip+'",\n    "status": "'+status+'"\n}\n'

    # Save log
    log = open(path, 'a')
    log.write(furme)
    log.close()
    root.destroy()


root = Tk()
root.title("Example")

label = Label(root, text="Waiting for task to finish.")
label.pack()

root.after(200, task)
root.mainloop()
