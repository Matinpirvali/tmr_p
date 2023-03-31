try:
    import platform
    import subprocess
    import requests

    from datetime import datetime
    from os import system
    from datetime import datetime
    from tkinter import *

    system('clear')
except ModuleNotFoundError:
    print('Script need Python3\nPelease install requirements : \nwith "pip install -r requirements.txt"')

class main:
    def log():
        #check network connection
        url='http://www.google.com/'
        timeout=5
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

        furme = '{\n    "time": "'+time_log+'",\n    "system": "'+platform_log+'",\n    "IP": "'+ip+'",\n    "status": "'+status+'"\n}\n'

        # Save log
        log = open(path, 'a')
        log.write(furme)
        log.close()

    def bot():
        def chat_panel_fa():
            root = Tk()
            root.title('TMR-P-fa')
            root.geometry('500x600')
            root.configure(bg="#2D2727")

            Banner = Label(text='TMR_P AI Bot', font=('bold', 30), fg='#8F43EE', bg='#2D2727').place(y=50 , x=120)


            mat = Entry(root, font=('bold', 20), bg='#413543', fg='#F0EB8D')
            mat.place(y=550, x=15)

            enter = Button(root, text='Enter', font=('bold', 20), bg='#8F43EE', fg='#F0EB8D')
            enter.place(y=545, x=370)

            root.mainloop()

        def chat_panel_en():
            root = Tk()
            root.title('TMR-P')
            root.geometry('500x600')
            root.configure(bg="#2D2727")

            Banner = Label(text='TMR_P AI Bot', font=('bold', 30),fg='#8F43EE', bg='#2D2727').place(y=50, x=120)

            mat = Entry(root, font=('bold', 20), bg='#413543', fg='#F0EB8D')
            mat.place(y=550, x=15)

            enter = Button(root, text='Enter', font=('bold', 20), bg='#8F43EE', fg='#F0EB8D')
            enter.place(y=545, x=370)

            root.mainloop()

        def settingup():
            settingup_p = Tk()
            settingup_p.title('Setting Up')
            settingup_p.geometry('400x550')
            settingup_p.configure(bg="#2D2727")

            Label(settingup_p, text='language', font=('bold', 30),
                  bg='#2D2727', fg='#F0EB8D').place(x=110, y=50)

            lang_fa = Button(settingup_p, text='Farsi', font=('bold', 30), bg='#2D2727', fg='#F0EB8D',command=chat_panel_fa)
            lang_fa.place(x=250,y=150)

            lang_en = Button(settingup_p, text='English', font=('bold', 30), bg='#2D2727', fg='#F0EB8D',command=chat_panel_en)
            lang_en.place(x=50, y=150)

            settingup_p.mainloop()
        
        settingup()
        

if __name__ == "__main__":
    main.bot()