import platform

if __name__ == "__main__":
    
    # System Guard
    osn = platform.system()
    if osn == 'Linux':
        print('System Guard Verifred os: {osn}')
    elif osn == 'Windows':
        print('System Guard Verifred os: {osn}')
    else:
        print('System Guard Not Verifred os: {osn}')