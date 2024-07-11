from utils.all_system_control import *
from utils.ANSI_color import *
from utils.system_control_protocol import *
from utils.string_processing import *







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
    print(f'            {get_color_str('Create New VENV', 'GREEN')}            ')
    print()




    if step == 'project_directory':
        if not first_time:
            print(f'{get_color_str('Please fill in the valid Directory Name', 'RED')}')
        
        sha_256_str = sha256_generator()
        print(f'sha256: {sha_256_str}')
        print('Paste this to answer to go back to main menu')
        print()
        print()
        print()
        project_directory = input(f'Libraries / Dependencies in requirements.txt (Y/n):{GO_UP_ONE_LINE}Project Name / Venv Name:{GO_UP_ONE_LINE}Project Directory: ')
        print()
        print()
        print()

        if project_directory == sha_256_str:
            return GO_BACK_TO_MENU_PAGE

        else:
            directory_exist = os.system(f'cd "{project_directory}"')
            if directory_exist == 0:
                return project_directory
            else:
                return None


    elif step == 'venv':


        if not first_time:
            print(f'{get_color_str('Please fill in the Venv Name', 'RED')}')
        
        sha_256_str = sha256_generator()
        print(f'sha256: {sha_256_str}')
        print('Paste this to answer to go back to main menu')
        print()
        print('Project Directory: ' + kwargs['project_directory'])
        print()
        

        project_name = input(f'Libraries / Dependencies in requirements.txt (Y/n):{GO_UP_ONE_LINE}Project Name / Venv Name: ')
        print()
        print()

        if project_name == sha_256_str:
            return GO_BACK_TO_MENU_PAGE
        else:
            return project_name
        

    elif step == 'requirement':
        if not first_time:
            print(f'{get_color_str('Please fill in the Valid Answer', 'RED')}')
        
        sha_256_str = sha256_generator()
        print(f'sha256: {sha_256_str}')
        print('Paste this to your answer to go back to main menu')
        print()
        print('Project Directory: ' + kwargs['project_directory'])
        print('Project Name / Venv Name: ' + kwargs['venv'])
        yes_no_requirement = input(f'Libraries / Dependencies in requirements.txt (Y/n): ')

        if yes_no_requirement == sha_256_str:
            return GO_BACK_TO_MENU_PAGE
        
        elif yes_no_requirement == 'Y' or yes_no_requirement == 'y':
            requirement_path = input('requirements.txt path: ')
            
            if requirement_path == None or requirement_path == '':
                return NO_REQUIREMENTS_FILE
            elif requirement_path == sha_256_str:
                return GO_BACK_TO_MENU_PAGE
            else:
                try:
                    with open(requirement_path, 'r') as f:
                        f.readline()
                except FileNotFoundError as e:
                    return None

            return requirement_path
        
        elif yes_no_requirement == 'N' or yes_no_requirement == 'n':
            return NO_REQUIREMENTS_FILE
        
        else:
            return None
        
    elif step == 'library_manual_input':

        if not first_time:
            print(f'{get_color_str('Please fill in the Valid Answer', 'RED')}')
        
        sha_256_str = sha256_generator()
        print(f'sha256: {sha_256_str}')
        print('Paste this to your answer to go back to main menu')
        print()
        print('Project Directory: ' + kwargs['project_directory'])
        print('Project Name / Venv Name: ' + kwargs['venv'])
        print(f'Libraries / Dependencies in requirements.txt (Y/n): n')
        yes_no_libraries = input('Set up venv with libraries (Y/n): ')

        if yes_no_libraries == sha_256_str:
            return GO_BACK_TO_MENU_PAGE
        
        elif yes_no_libraries == 'Y' or yes_no_libraries == 'y':
            libraries = input('Libraries: ')

            if libraries == None or libraries == '':
                return NO_LIBRARIES
            elif libraries == sha_256_str:
                return GO_BACK_TO_MENU_PAGE

            libraries = str_to_list(libraries)
            libraries = list_to_str(libraries, sep = ' ')
        
        elif yes_no_libraries == 'N' or yes_no_libraries == 'n':
            return NO_LIBRARIES

        else:
            return None


        return libraries
    

def view_venv_info_screen(first_time = True, step = None, *arg, **kwargs):
    introduction_screen()
    print(f'         {get_color_str('View VENV Details', 'GREEN')}            ')
    print()

    if step == 'view_venv_menu':
        view_choice = [inquirer.List('view_choice', message = 'Options', choices = [
            '1. View All Venv',
            '2. View 10 Recently Created Venv',
            '3. Edit Venv',
            '4. Back'
        ], default = '1. View All Venv')]

        user_answer = inquirer.prompt(view_choice, theme = GreenPassion())['view_choice']

        if user_answer[0] == '4':
            clear_screen()
            return False
        
        return user_answer[0]






def menu_screen():
    print(f'              {get_color_str('MENU', 'GREEN')}                     ')
    print()
    menu_choice = [inquirer.List('menu_choice', message = 'Options', choices = [
        '1. Create New Project',
        '2. View Created Virtual Enviroment',
        '3. Settings',
        '4. Exit'
    ], default = '1. Create New Project')]
    user_answer = inquirer.prompt(menu_choice, theme = GreenPassion())['menu_choice']

    display_functions = [create_new_project_screen, view_venv_info_screen]

    end_program = menu_choice_process(user_answer[0], display_functions)
    # print(user_answer[0])





    if user_answer[0] == '4':
        clear_screen()
        return True
    
    return end_program