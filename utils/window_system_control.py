import os
from commands.window_command import *

def clear_screen():
    return_status = os.system(clear_screen_command)

def create_venv(project_directory, project_name):
    os.system(f'cd "{project_directory}"\n' + CREATE_VENV + project_name)

def install_libraries(project_directory, venv, libraries):
    os.system(f'cd "{project_directory}"\n' + venv + '\\Scripts\\activate.bat\npip install ' + libraries)
    