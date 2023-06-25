# BDadmehr0 - Garfox
try:
    import platform
    import subprocess
    import requests
    import time
    import threading

    from tkinter import ttk
    from tkinter import *
    from customtkinter import *
    from datetime import datetime
    from os import system

    # from lib import sound_ef
    from lib.lin import run_l
    from lib.pages import loading_page
except ModuleNotFoundError:
    try:
        system('pip3 install datetime')
        system('pip3 install requests')
        system('pip3 install playsound')
        system('pip3 install customtkinter')
    except:
        print('install fail')



def run_w():
    # APP Theme
    set_default_color_theme("dark-blue")

    def about():
        pass

    def button_send_main():
        def button_send_task():
            pass

        if 1 == 1:
            button_send_main()

    home = CTk()
    home.title('TMR_P')
    home.geometry('600x600')
    home.resizable(width=False, height=False)

    # BOT Aseets
    frame_bot = CTkFrame(home)
    frame_bot.pack(padx=10, pady=12, fill=X)

    bot_tit_lb = CTkLabel(frame_bot, text='Bot', font=('Roboto', 25), corner_radius=0)
    bot_tit_lb.pack(padx=12, pady=12, side=TOP)

    bot_lb = CTkLabel(frame_bot, text='سلام', font=('Roboto', 20), corner_radius=0)
    bot_lb.pack(padx=12, pady=12, side=LEFT)

    # Other
    About_btn = CTkButton(frame_bot, text='About', corner_radius=0)
    About_btn.pack(side=RIGHT)

    # User
    frame_user = CTkFrame(home)
    frame_user.pack(padx=10, pady=12, fill=X, side=BOTTOM)

    qust_user_ent = CTkEntry(frame_user, width=500, font=('Bold', 25), corner_radius=0)
    qust_user_ent.pack(side=LEFT)

    send_btn = CTkButton(frame_user, text='✔️', font=('bold', 25), corner_radius=0, command=button_send_main)
    send_btn.pack(side=LEFT)

    home.mainloop()

    # def log():
    #     def simulate_loading():
    #         # check network connection
    #         url = 'http://www.google.com/'
    #         timeout = 5
    #         status = ''

    #         try:
    #             _ = requests.head(url, timeout=timeout)
    #             status += 'Online'
    #         except requests.ConnectionError:
    #             status += 'Offline'
    #             print("No internet connection available.")
    #             return False

    #         # Get ip public
    #         ip = requests.get('https://api.ipify.org').text

    #         # Time & platform
    #         time_log = str(datetime.now())
    #         platform_log = str(platform.platform())
    #         path = 'log//log.json'

    #         furme = '{\n    "time": "' + time_log + '",\n    "system": "' + platform_log + '",\n    "IP": "' + ip + '",\n    "status": "' + status + '"\n}\n'

    #         # Save log
    #         log = open(path, 'w')
    #         log.write(furme)
    #         log.close()

if __name__ == "__main__":
    # System Guard

    osn = platform.system()
    if osn == 'Linux':
        print(f'System Guard Verifred os: {osn}')
        run_loading = loading_page.loading_page()
        run_l()
    elif osn == 'Windows':
        print(f'System Guard Verifred os: {osn}')
        run_loading = loading_page.loading_page()
        run_w()
    else:
        print(f'System Guard Not Verifred os: {osn}')
