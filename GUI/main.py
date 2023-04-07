try:
    import platform
    import subprocess
    import requests
    import time

    from os import system
    from datetime import datetime
    from tkinter import *
    from PIL import ImageTk, Image

    system('clear')
except ModuleNotFoundError:
    print('Script need Python3\nPelease install requirements : \nwith "pip install -r requirements.txt"')

class main:
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

            furme = '{\n    "time": "'+time_log+'",\n    "system": "' + \
                platform_log+'",\n    "IP": "'+ip+'",\n    "status": "'+status+'"\n}\n'

            # Save log
            log = open(path, 'a')
            log.write(furme)
            log.close()
            root.destroy()
        # Load page tk
        root = Tk()
        root.title("Example")

        label = Label(root, text="Waiting for task to finish.")
        label.pack()

        root.after(200, task)
        root.mainloop()


    def main_bot():
        class bot:

            def chat_panel():
                hig_bot = 450
                hig_you = 400

                def your_req():
                    Question = mat.get()
                    print('Question: ', Question)
                    len_ques = len(Question)
                    Your_Chat.config(text=Question)

                root = Tk()
                # config UI
                root.title('TMR-P')
                root.geometry('500x600')
                root.configure(bg="#2D2727")

                Label(text='TMR_P AI Bot', font=('bold', 30), fg='#8F43EE', bg='#2D2727').place(y=30, x=120)

                # input

                mat = Entry(root, font=('bold', 20),bg='#413543', fg='#F0EB8D')
                mat.place(y=550, x=15)

                # Enter Btn

                enter = Button(root, text='Enter', font=('bold', 20), bg='#8F43EE', fg='#F0EB8D', command=your_req)
                enter.place(y=545, x=370)

                # Chat texts

                Bot_Chat = Label(root, text='bot', font=("Helvetica", 15), bg='#2D2727', fg='#F0EB8D')
                Bot_Chat.place(x=40, y=hig_bot)

                Your_Chat = Label(root, text='you', font=("Helvetica", 15), bg='#2D2727', fg='#F0EB8D')
                Your_Chat.place(x=400, y=hig_you)

                info_btn = Button(root, text='Info')
                info_btn.place(x=15,y=20)

                root.mainloop()

        if __name__ == "__main__":
            bot.chat_panel()
        

if __name__ == "__main__":
    main.log()
    main.main_bot()