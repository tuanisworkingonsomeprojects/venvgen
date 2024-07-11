from utils.system_control_protocol import *
import sqlite3 
from utils.database_manager import *
from datetime import date



def option1(display_function, *args, **kwargs):
    con = sqlite3.connect('venv_database.db')
    check_database(con)

    first_time = True
    project_directory = None

    while first_time or (not first_time and (project_directory == None or project_directory == '')):
        project_directory = display_function(first_time, 'project_directory')
        first_time = False
    
        if project_directory == GO_BACK_TO_MENU_PAGE:
            return False
    
    first_time = True
    venv_name = None
    
    while first_time or (not first_time and (venv_name == None or venv_name == '')):
        venv_name = display_function(first_time, 'venv', project_directory = project_directory)
        first_time = False

        if venv_name == GO_BACK_TO_MENU_PAGE:
            return False
        
    first_time = True
    require_name = None

    while first_time or (not first_time and (require_name == None or require_name == '')):
        require_name = display_function(first_time, 'requirement', venv = venv_name, project_directory = project_directory)
        first_time = False

        if require_name == GO_BACK_TO_MENU_PAGE:
            return False
        
        if require_name != NO_REQUIREMENTS_FILE:
            try:
                with open(require_name, 'r') as f:
                    f.readline()
            except FileNotFoundError as e:
                require_name = None
    
    if require_name == NO_REQUIREMENTS_FILE:
        first_time = True
        libraries = None

        while first_time or (not first_time and (libraries == None or libraries == '')):
            libraries = display_function(first_time, 'library_manual_input', venv = venv_name, project_directory = project_directory)
            first_time = False

            if libraries == GO_BACK_TO_MENU_PAGE:
                return False

        kwargs['system_control'].create_venv(project_directory, venv_name)

        if libraries != NO_LIBRARIES:
            kwargs['system_control'].install_libraries(project_directory, venv_name, libraries)
        return False
    
    if require_name != NO_REQUIREMENTS_FILE:
        kwargs['system_control'].create_venv(project_directory, venv_name)
        kwargs['system_control'].install_libraries_with_requirement(project_directory, venv_name, require_name)
        insert_into_venv_info_sql(con, project_path = project_directory, venv_name = venv_name, created_date = date.today(), require_file = require_name)
        


    else:
        kwargs['system_control'].create_venv(project_directory, venv_name)
        insert_into_venv_info_sql(con, project_path = project_directory, venv_name = venv_name, created_date = date.today(), require_file = None)

    con.close()
    
def option2(display_function, *args, **kwargs):
    con = sqlite3.connect('venv_database.db')

    check_database(con)







    pass