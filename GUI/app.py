try:
    import platform
    import subprocess
    import datetime
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
        url='http://www.google.com/'
        timeout=5
        status = ''

        try:
            _ = requests.head(url, timeout=timeout)
            status += 'Online'
        except requests.ConnectionError:
            status += 'Offline'
            print("No internet connection available.")
        
        #Ip
        ip = requests.get('https://api.ipify.org').text

        # Time & platform 
        time_log = datetime.date.today()
        platform_log = str(platform.platform())
        path = 'data/log.json'

        furme = '{\n    "time": "'+time_log+'",\n    "system": "'+platform_log+'",\n    "IP": "'+ip+'",\n    "status": "'+status+'"\n}\n'

        # Save log
        log = open(path, 'a')
        log.write(furme)
        log.close()

    def Bot():
        my_list = ["english", "English", "persian", "Persian"]
        n=0

        root = Tk()
        root.title('TMR-P')
        root.geometry('500x600')
        root.configure(bg="#2D2727")

        Banner = Label(text='TMR_P AI Bot', font=('bold', 30), fg='#8F43EE', bg='#2D2727').place(y=50 , x=120)


        mat = Entry(root, font=('bold', 20), bg='#413543', fg='#F0EB8D')
        mat.place(y=550, x=15)

        enter = Button(root, text='Enter', font=('bold', 20), bg='#8F43EE', fg='#F0EB8D')
        enter.place(y=545, x=370)

        root.mainloop()

if __name__ == "__main__":
    main.log()