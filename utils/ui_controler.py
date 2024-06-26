from utils.all_system_control import check_system, check_ui_library, get_this_project_version
from utils.ANSI_color import get_color_str, print_color






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

def menu_screen():
    print(f'              {get_color_str('MENU', 'GREEN')}                     ')
    print()
    menu_choice = [inquirer.List('menu_choice', message = 'Options', choices = [
        '1. Create New Project',
        '2. View All Created Virtual Enviroment',
        '3. Settings',
        '4. Exit'
    ], default = '1. Create New Project')]
    answer = inquirer.prompt(menu_choice, theme = GreenPassion())['menu_choice']

    print(answer)

    return True