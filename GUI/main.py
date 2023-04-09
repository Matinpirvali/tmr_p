try:
    from lib import lin
    from lib import win

    from platform import system
except:
    print('Script need Python3\nPelease install requirements : with "pip install -r requirements.txt\n"')

def system_check():
    name_OS = system()

    if name_OS == 'Linux':
        lin.linux_v()
    elif name_OS == "Windows":
        win.windows_v()
    else:
        print("App not suport your system")


system_check()