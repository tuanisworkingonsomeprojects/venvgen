from utils.system_control_protocol import *



def option1(user_answer, display_function):
    first_time = True
    venv_name = None
    
    while first_time or (not first_time and (venv_name == None or venv_name == '')):
        venv_name = display_function(first_time, 'venv')
        first_time = False

        if venv_name == GO_BACK_TO_MENU_PAGE:
            return False
        
    first_time = True
    require_name = None

    while first_time or (not first_time and (require_name == None or require_name == '')):
        require_name = display_function(first_time, 'requirement', venv = venv_name)
        first_time = False

        if require_name == GO_BACK_TO_MENU_PAGE:
            return False
    
    if require_name == NO_REQUIREMENTS_FILE:
        input()
        return False