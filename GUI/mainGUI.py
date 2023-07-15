# BDadmehr0 - Garfox

import platform

from customtkinter import *
from datetime import datetime

# from lib import sound_ef
from lib.Python_information import science
from lib.pages import loading_page
from lib.lin import run_l
from lib.win import run_w

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
