import platform
import os
from utils.ANSI_color import *
__version__ = '1.0'



def check_system():
    if platform.system() == 'Darwin':
        return 'macos'
    elif platform.system() == 'win32' or platform.system() == 'Windows':
        return 'win'
    
def check_ui_library():
    try:
        import inquirer
    except ModuleNotFoundError as e:
        print()
        print(f'{get_color_str('inquirer', 'RED')} module have not yet installed')
        print()
        print('Do you want to download it to your machine?')
        print()
        print('The library is Required for the program to run')
        userChoice = input('Your choice (Y/n): ')
        if userChoice == 'Y' or userChoice == 'y':
            os.system('pip install inquirer')
            print()
            print('Please rerun the program after installation')
            exit()        
        else:
            print()
            print_color('Cannot process further due to lack of library', 'RED')
            exit()
    
        
def get_this_project_version():
    return __version__