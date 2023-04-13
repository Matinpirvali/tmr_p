try:
    import platform
    import os
    from lib import sound_ef
except:
    print('Script need Python3\nPelease install requirements : with "pip install -r requirements.txt\n"')
name_OS = platform.system()

sound_ef.Effect(mode='ok')

class main:
    def install_update():
        global name_OS
        if name_OS == 'Linux':
            try:
                os.system('pip3 install datetime')
                os.system('pip3 install requests')
                os.system('pip3 install playsound')

                os.system('clear')
            except:
                pass
        elif name_OS == 'Windows':
            try:
                os.system('pip3 install datetime')
                os.system('pip3 install requests')
                os.system('pip3 install playsound')
            except:
                print('install Fail')

            os.system('cls')
        else:
            print('App not suport your system')

    def run():
        global name_OS

        if name_OS == 'Linux':
            # Lunch app
            os.system('python3 lin.py')

        elif name_OS == "Windows":
            # Lunch app
            os.system('python3 win.py')
        else:
            print("App not suport your system")

if __name__ == "__main__":
    main.install_update():
    main.run()
