from ..general.ANSI_color import get_color_str
from ..general.ui_helper import introduction_screen, print_current_page


OPTION2_NAVIGATION     = 'menu > view venv details'
OPTION2_1_NAVIGATION   = f'{OPTION2_NAVIGATION} > view all venv'
OPTION2_2_NAVIGATION   = f'{OPTION2_NAVIGATION} > view venv (filtered)'
OPTION2_2_1_NAVIGATION = f'{OPTION2_2_NAVIGATION} > view latest created date'
OPTION2_2_2_NAVIGATION = f'{OPTION2_2_NAVIGATION} > view latest modified time'
OPTION2_2_3_NAVIGATION = f'{OPTION2_2_NAVIGATION} > view earliest created date'
OPTION2_2_4_NAVIGATION = f'{OPTION2_2_NAVIGATION} > view earliest modified time'
OPTION2_3_NAVIGATION   = f'{OPTION2_NAVIGATION} > venv details'
OPTION2_4_NAVIGATION   = f'{OPTION2_NAVIGATION} > venv edit'

OPTION2_HEADER     = f'              {get_color_str('View Venv Details', 'GREEN')}'
OPTION2_1_HEADER   = f'                {get_color_str('View All VENV', 'GREEN')}'
OPRION2_2_HEADER   = f'             {get_color_str('View Venv (filtered)', 'GREEN')}'
OPTION2_2_1_HEADER = f'     {get_color_str('View VENV (Sorted By Latest Created Date)', 'GREEN')}'
OPTION2_2_2_HEADER = f'     {get_color_str('View VENV (Sorted By Latest Modified Time)', 'GREEN')}'
OPTION2_2_3_HEADER = f'    {get_color_str('View VENV (Sorted By Earliest Created Date)', 'GREEN')}'
OPTION2_2_4_HEADER = f'    {get_color_str('View VENV (Sorted By Earliest Modified Time)', 'GREEN')}            '


def 