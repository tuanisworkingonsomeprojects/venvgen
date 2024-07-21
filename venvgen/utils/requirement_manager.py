from . import OS
from .package_directory_manager import get_requirement_dir, create_requirement_dir
from .database_manager import select_the_latest_inserted_venv_id

import os

def check_requirement():
    create_requirement_dir()

def requirement_generator(project_dir, venv):
    requirement_dir = get_requirement_dir()
    latest_inserted_id = select_the_latest_inserted_venv_id()
    pip_freeze = OS.get_requirement(project_dir, venv)

    with open(os.path.join(requirement_dir, f'{latest_inserted_id}.txt'), 'w') as f:
        f.write(pip_freeze)

    return latest_inserted_id, os.path.join(requirement_dir, f'{latest_inserted_id}.txt')

def requirement_is_updated(venv_id, project_dir, venv):
    requirement_dir = get_requirement_dir()
    latest_inserted_id = select_the_latest_inserted_venv_id()
    pip_freeze = OS.get_requirement(project_dir, venv)

    with open(os.path.join(requirement_dir, f'{latest_inserted_id}.txt'), 'r') as f:
        requirement_file = f.read(pip_freeze)

    if pip_freeze == requirement_file:
        return True
    else:
        return False

    