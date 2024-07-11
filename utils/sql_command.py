create_venv_info_sql = '''
CREATE TABLE IF NOT EXISTS venv_info(
    id INT PRIMARY KEY ASC AUTOINCREMENT,
    project_path VARCHAR(300) NOT NULL,
    venv_name VARCHAR(200) NOT NULL,
    created_date DATE NOT NULL,
    requirement_file VARCHAR(300)
);
'''

insert_into_venv_info_sql = '''
INSERT INTO venv_info(project_path, venv_name, created_date, requirement_file) VALUES (?, ?, ?, ?);
'''