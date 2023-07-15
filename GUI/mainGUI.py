# BDadmehr0 - Garfox

import platform

from customtkinter import *
from datetime import datetime
from os import system

# from lib import sound_ef
from lib.assets.Python_information import science
from lib.lin import run_l
from lib.pages import loading_page

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
