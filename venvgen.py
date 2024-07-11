from utils.ui_controler import *
from utils.all_system_control import check_system
import warnings
warnings.filterwarnings("ignore")

THIS_MACHINE = check_system()
end_program = False

while not end_program:
    introduction_screen()
    end_program = menu_screen()





