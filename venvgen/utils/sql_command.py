CREATE_VENV_INFO_SQL = '''
CREATE TABLE IF NOT EXISTS venv_info(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    project_path VARCHAR(300) NOT NULL,
    venv_name VARCHAR(200) NOT NULL,
    created_date DATE NOT NULL,
    requirement_file VARCHAR(300),
    connect_status VARCHAR(20) NOT NULL,
    last_modified DATETIME NOT NULL,
    UNIQUE(project_path, venv_name)
);
'''

CREATE_VENV_LOG_SQL = '''
CREATE TABLE IF NOT EXISTS venv_log(
    id INTEGER PRIMARY KEY ASC AUTOINCREMENT,
    venv_id INTEGER NOT NULL,
    modify_type VARCHAR(30) NOT NULL,
    modify_time DATETIME NOT NULL,
    modified_by VARCHAR(20) NOT NULL,
    FOREIGN KEY (venv_id) REFERENCES venv_info(id) ON DELETE NO ACTION
);
'''

CREATE_VENV_INSERT_TRIGGER_LOG_SQL = '''
CREATE TRIGGER IF NOT EXISTS venv_insert_info_trigger
AFTER INSERT ON venv_info
FOR EACH ROW
BEGIN 
    INSERT INTO venv_log(venv_id, modify_type, modify_time, modified_by)
    VALUES (NEW.id, 'INSERT VENV', DATETIME('now', 'localtime'), 'USER');
END;
'''

CREATE_VENV_UPDATE_STATUS_TRIGGER_LOG_SQL = '''
CREATE TRIGGER IF NOT EXISTS venv_status_update_trigger
AFTER UPDATE OF connect_status ON venv_info
FOR EACH ROW
BEGIN
    INSERT INTO venv_log(venv_id, modify_type, modify_time, modified_by)
    VALUES (NEW.id, 'UPDATE CONNECTION STATUS', DATETIME('now', 'localtime'), 'SYSTEM');
END;
'''



INSERT_INTO_VENV_INFO_SQL = '''
INSERT INTO venv_info(project_path, venv_name, created_date, requirement_file, connect_status, last_modified) 
VALUES (?, ?, ?, ?, ?, ?);
'''

UPDATE_CONNECT_STATUS_VENV_INFO_SQL = '''
UPDATE venv_info
SET connect_status = ?,
    last_modified = ?
WHERE id = ?;
'''

SELECT_ALL_VENV_SQL = '''
SELECT id AS [VENV ID],
       venv_name AS [VENV],
       created_date AS [CREATED DATE],
       connect_status AS [CONNECTION STATUS],
       project_path AS [PROJECT DIR],
       last_modified AS [LAST MODIFIED]
FROM   venv_info;
'''

SELECT_LATEST_CREATE_DATE_VENV_SQL = '''
SELECT id AS [VENV ID],
       venv_name AS [VENV],
       created_date AS [CREATED DATE],
       connect_status AS [CONNECTION STATUS],
       project_path AS [PROJECT DIR],
       last_modified AS [LAST MODIFIED]
FROM   venv_info
ORDER BY created_date DESC;
'''

SELECT_TOP_LATEST_CREATE_DATA_VENV_SQL = '''
SELECT id AS [VENV ID],
       venv_name AS [VENV],
       created_date AS [CREATED DATE],
       connect_status AS [CONNECTION STATUS],
       project_path AS [PROJECT DIR],
       last_modified AS [LAST MODIFIED]
FROM   venv_info
ORDER BY created_date DESC
LIMIT ?;
'''

SELECT_TOP_LATEST_MODIFIED_DATA_VENV_SQL = '''
SELECT id AS [VENV ID],
       venv_name AS [VENV],
       created_date AS [CREATED DATE],
       connect_status AS [CONNECTION STATUS],
       project_path AS [PROJECT DIR],
       last_modified AS [LAST MODIFIED]
FROM   venv_info
ORDER BY last_modified DESC
LIMIT ?;
'''

SELECT_TOP_EARLIEST_CREATE_DATA_VENV_SQL = '''
SELECT id AS [VENV ID],
       venv_name AS [VENV],
       created_date AS [CREATED DATE],
       connect_status AS [CONNECTION STATUS],
       project_path AS [PROJECT DIR],
       last_modified AS [LAST MODIFIED]
FROM   venv_info
ORDER BY created_date
LIMIT ?;
'''

SELECT_TOP_EARLIEST_MODIFIED_DATA_VENV_VIEW = '''
SELECT id AS [VENV ID],
       venv_name AS [VENV],
       created_date AS [CREATED DATE],
       connect_status AS [CONNECTION STATUS],
       project_path AS [PROJECT DIR],
       last_modified AS [LAST MODIFIED]
FROM   venv_info
ORDER BY last_modified
LIMIT ?;
'''

SELECT_SPECIFIC_VENV_SQL = '''
SELECT id AS [VENV ID],
       venv_name AS [VENV],
       created_date AS [CREATED DATE],
       connect_status AS [CONNECTION STATUS],
       project_path AS [PROJECT DIR],
       last_modified AS [LAST MODIFIED]
FROM   venv_info
WHERE  id = ?;
'''