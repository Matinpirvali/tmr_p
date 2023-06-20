import platform

if __name__ == "__main__":
    
    # System Guard
    osn = platform.system()
    if osn == 'Linux':
        print(f'System Guard Verifred os: {osn}')
    elif osn == 'Windows':
        print(f'System Guard Verifred os: {osn}')
    else:
        print(f'System Guard Not Verifred os: {osn}')