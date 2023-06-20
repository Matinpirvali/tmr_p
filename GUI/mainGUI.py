import platform
from lib.lin import run_l
from lib.win import run_w

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