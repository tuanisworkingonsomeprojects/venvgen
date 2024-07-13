from . import OS



def introduction_screen():
    check_system()
    clear_screen()
    print('_______________________________________')
    print(f'        {get_color_str('Python VENV Generator', 'GREEN')}     ')
    print()
    print(f' This Version:\t{get_this_project_version()}')
    print(' Created By:\tNguyen Tuan')
    print(f' Your OS:\t{check_system()}')
    print('_______________________________________')