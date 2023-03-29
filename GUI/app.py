try:
    from datetime import datetime
    import os
    import platform
    import subprocess
    from datetime import datetime
    from tkinter import *
    import requests
except ModuleNotFoundError:
    print('Pelease install requirements.txt\nwith "pip install -r requirements.txt"')


class main:
    
    def log():
        time_log = str(datetime.now())
        platform_log = str(platform.platform())
        path = 'data/log.json'

        furme = '{\n    "time": "'+time_log+'",\n    "system": "'+platform_log+'"\n}\n'

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
    main.Bot()