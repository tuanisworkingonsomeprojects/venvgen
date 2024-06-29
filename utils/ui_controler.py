from utils.all_system_control import *
from utils.ANSI_color import *
from utils.system_control_protocol import *
import random
import hashlib







if __name__ == 'utils.ui_controler':
    print('\n\n\n\n\n\n\n\n\n')
    print('Checking UI system...')
    check_ui_library()
    import inquirer
    from inquirer.themes import GreenPassion

    print('Checking Operating System...')
    if check_system() == 'macos':
        from utils.macos_system_control import *
    elif check_system() == 'win':
        from utils.window_system_control import *
    from utils.ANSI_line_modification import *

    

def test_name():
    print(__name__)


def introduction_screen():
    clear_screen()
    print('_______________________________________')
    print(f'        {get_color_str('Python VENV Generator', 'GREEN')}     ')
    print()
    print(f' This Version:\t{get_this_project_version()}')
    print(' Created By:\tNguyen Tuan')
    print(f' Your OS:\t{check_system()}')
    print('_______________________________________')


def create_new_project_screen(first_time = True, step = 'venv', *args, **kwargs):
    introduction_screen()
    print(f'         {get_color_str('Create New Project', 'GREEN')}            ')
    print()

    if step == 'venv':


        if not first_time:
            print(f'{get_color_str('Please fill in the Venv Name', 'RED')}')
        
        sha_256_str = sha256_generator()
        print(f'sha256: {sha_256_str}')
        print('Paste this to answer to go back to main menu')
        print()
        print()
        

        project_name = input(f'Create with requirements.txt (Y/n):{GO_UP_ONE_LINE}Project Name / Venv Name: ')
        print()
        print()

        if project_name == sha_256_str:
            return 'asgjqpo3irht=0239r1p93q8yrtiogwehjknldfmbnq24[e0dp9touiq3fj1kqrmwefglobwdk.jsnfbvc efgdboqkelt;nrfg,bwopeust;dhjflgknwmepstdofgjblvkwelargjksfhdnw.vearspg]'
        else:
            return project_name
        

    elif step == 'requirement':
        if not first_time:
            print(f'{get_color_str('Please fill in the Valid Answer', 'RED')}')
        
        sha_256_str = sha256_generator()
        print(f'sha256: {sha_256_str}')
        print('Paste this to your answer to go back to main menu')
        print()
        print('Project Name / Venv Name: ' + kwargs['venv'])
        yes_no_requirement = input(f'Create with requirements.txt (Y/n): ')

        if yes_no_requirement == sha_256_str:
            return GO_BACK_TO_MENU_PAGE
        
        elif yes_no_requirement == 'Y' or yes_no_requirement == 'y':
            requirement_path = input('requirements.txt path: ')
            
            if requirement_path == None or requirement_path == '':
                return NO_REQUIREMENTS_FILE
            elif requirement_path == sha_256_str:
                return GO_BACK_TO_MENU_PAGE

            return requirement_path
        
        elif yes_no_requirement == 'N' or yes_no_requirement == 'n':
            return NO_REQUIREMENTS_FILE
        
        else:
            return None




        return 'abc'

def menu_screen():
    print(f'              {get_color_str('MENU', 'GREEN')}                     ')
    print()
    menu_choice = [inquirer.List('menu_choice', message = 'Options', choices = [
        '1. Create New Project',
        '2. View All Created Virtual Enviroment',
        '3. Settings',
        '4. Exit'
    ], default = '1. Create New Project')]
    user_answer = inquirer.prompt(menu_choice, theme = GreenPassion())['menu_choice']

    end_program = menu_choice_process(user_answer[0], create_new_project_screen)
    # print(user_answer[0])





    if user_answer[0] == '4':
        return True
    
    return end_program