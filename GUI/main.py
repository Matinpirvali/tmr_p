try:
    import platform
    import subprocess
    import requests

    from datetime import datetime
    from os import system
    from datetime import datetime
    from tkinter import *
    from PIL import ImageTk, Image

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

    def main_bot():
        class bot:

            def chat_panel_fa():
                settingup_p.destroy()
                root = Tk()
                root.title('TMR-P-fa')
                root.geometry('500x600')
                root.configure(bg="#2D2727")

                Banner = Label(text='TMR_P AI Bot', font=('bold', 30),fg='#8F43EE', bg='#2D2727').place(y=50, x=120)

                mat = Entry(root, font=('bold', 20), bg='#413543', fg='#F0EB8D')
                mat.place(y=550, x=15)

                enter = Button(root, text='ارسال', font=('bold', 20), bg='#8F43EE', fg='#F0EB8D')
                enter.place(y=545, x=370)

                root.mainloop()


            def chat_panel_en():
                def your_req():
                    Question = mat.get()
                    print('Question: ', Question)
                    Your_Chat.config(text=Question)

                hig_bot = 450
                hig_you = 400

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

                #info icon
                frame = Frame(root, width=600, height=400)
                frame.pack()
                frame.place(anchor='center', relx=0.5, rely=0.5)

                # Create an object of tkinter ImageTk
                img = ImageTk.PhotoImage(Image.open("assets/img/info.png"))

                # Create a Label Widget to display the text or Image
                label = Label(frame, image=img)
                label.pack()

                root.mainloop()

            def settingup():
                # Chat Farsi

                # # Panel chose lang
                # settingup_p = Tk()
                # settingup_p.title('Setting Up')
                # settingup_p.geometry('400x300')
                # settingup_p.configure(bg="#2D2727")

                # Label(settingup_p, text='language', font=('bold', 30),
                #       bg='#2D2727', fg='#F0EB8D').place(x=110, y=50)

                # lang_fa = Button(settingup_p, text='Fa', font=('bold', 30), bg='#2D2727', fg='#F0EB8D',)
                # lang_fa.place(x=250, y=150)

                # lang_en = Button(settingup_p, text='En', font=('bold', 30), bg='#2D2727', fg='#F0EB8D', command=chat_panel_en)
                # lang_en.place(x=90, y=150)

                # settingup_p.mainloop()
                pass

        if __name__ == "__main__":
            bot.settingup()
            bot.chat_panel_en()
        

if __name__ == "__main__":
    main.main_bot()