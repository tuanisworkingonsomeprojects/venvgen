from utils.system_control_protocol import *




def option1(user_answer, display_function, *args, **kwargs):
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
        first_time = True
        libraries = None

        while first_time or (not first_time and (libraries == None or libraries == '')):
            libraries = display_function(first_time, 'library_manual_input', venv = venv_name)
            first_time = False

            if libraries == GO_BACK_TO_MENU_PAGE:
                return False

        kwargs['system_control'].create_venv(venv_name)

        if libraries != NO_LIBRARIES:
            kwargs['system_control'].install_libraries(venv_name, libraries)


        return False
    else:
        kwargs['system_control'].create_venv(venv_name)

    