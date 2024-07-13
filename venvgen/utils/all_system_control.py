# from utils.ANSI_color import *
# from utils.system_control_protocol import *
# from utils.option_manager import *
# from utils import macos_system_control as MacOS
# from utils import window_system_control as Windows

from . import OS
# from .system_control_protocol import *
from .option_manager import option1, option2
import random
import hashlib





# def check_system():
#     create_database_dir()
#     check_venv_connection(OS)
#     if platform.system() == 'Darwin': 
#         return 'macos'
#     elif platform.system() == 'win32' or platform.system() == 'Windows':
#         return 'win'
    
    
    
    
# def check_ui_library():
#     try:
#         import inquirer
#     except ModuleNotFoundError as e:
#         print()
#         print(f'{get_color_str('inquirer', 'RED')} module have not yet installed')
#         print()
#         print('Do you want to download it to your machine?')
#         print()
#         print('The library is Required for the program to run')
#         userChoice = input('Your choice (Y/n): ')
#         if userChoice == 'Y' or userChoice == 'y':
#             subprocess.run('pip install inquirer'.split(), shell = True)
#             print()
#             print('Please rerun the program after installation')
#             exit()        
#         else:
#             print()
#             print_color('Cannot process further due to the lack of library', 'RED')
#             exit()

#     try:
#         import pandas
#     except ModuleNotFoundError as e:
#         print()
#         print(f'{get_color_str('pandas', 'RED')} module have not yet installed')
#         print()
#         print('Do you want to download it to your machine?')
#         print()
#         print('The library is Required for the program to run')
#         userChoice = input('Your choice (Y/n): ')
#         if userChoice == 'Y' or userChoice == 'y':
#             subprocess.run('pip install inquirer'.split(), shell = True)
#             print()
#             print('Please rerun the program after installation')
#             exit()        
#         else:
#             print()
#             print_color('Cannot process further due to the lack of library', 'RED')
#             exit()

#     try:
#         import tabulate
#     except ModuleNotFoundError as e:
#         print()
#         print(f'{get_color_str('tabulate', 'RED')} module have not yet installed')
#         print()
#         print('Do you want to download it to your machine?')
#         print()
#         print('The library is Required for the program to run')
#         userChoice = input('Your choice (Y/n): ')
#         if userChoice == 'Y' or userChoice == 'y':
#             subprocess.run('pip install tabulate'.split(), shell = True)
#             print()
#             print('Please rerun the program after installation')
#             exit()        
#         else:
#             print()
#             print_color('Cannot process further due to the lack of library', 'RED')
#             exit()

def sha256_generator():
    return hashlib.sha256(str(random.randint(-100000000000, 10000000000000)).encode('utf-8')).hexdigest()


    

def menu_choice_process(user_answer, display_function):
    if user_answer == '1':
        return option1(display_function[0], system_control = OS)
    elif user_answer == '2':
        return option2(display_function[1], system_control = OS)


