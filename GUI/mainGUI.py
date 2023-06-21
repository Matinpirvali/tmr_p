import platform
from lib.lin import run_l
from lib.win import run_w
from os import system

def installion()
    try:
        system('pip3 install datetime')
        system('pip3 install requests')
        system('pip3 install playsound')
        system('pip3 install customtkinter')
    except:
        print('install fail')

if __name__ == "__main__":
    # System Guard
    osn = platform.system()
    if osn == 'Linux':
        print(f'System Guard Verifred os: {osn}')
        run_l()
    elif osn == 'Windows':
        print(f'System Guard Verifred os: {osn}')
        run_w()
    else:
        print(f'System Guard Not Verifred os: {osn}')
