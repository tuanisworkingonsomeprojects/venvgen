import os
from commands.macos_command import *


def clear_screen():
    return_status = os.system(clear_screen_command)

def create_venv(project_name):
    os.system(create_venv + 'project_name')

def install_libraries(venv, libraries):
    os.system('source ' + venv + '/bin/activate\npip install ' + libraries)