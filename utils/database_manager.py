import sqlite3
import pandas as pd
from utils.sql_command import *


'''
Database:

venv_info(id, project_path, venv_name, created_date, requirement_file)

'''

def check_database(con):
    cur = con.cursor()
    cur.execute(create_venv_info_sql)



def insert_data(con: sqlite3.Connection, *args, **kwargs):
    cur = con.cursor()
    cur.execute(insert_into_venv_info_sql, (kwargs['project_path'], kwargs['venv_name'], kwargs['created_date'], kwargs['requirement_file']))
    con.commit()

