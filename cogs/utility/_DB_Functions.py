import sqlite3
from pathlib import Path, PurePath
from Hephaestus.logs.logger import log_debug, log_info, log_critical
from __main__ import config


current_dir = Path(__file__).parent.resolve()
cogs_folder = current_dir.parent
main_folder = cogs_folder.parent
conn = sqlite3.connect(PurePath(main_folder, config['Database_name']))
log_debug(f"Database file located at {PurePath(main_folder, config['Database_name'])}")
c = conn.cursor()


def give_points(_USER_ID, _NUM_POINTS):
    c.execute('''
        UPDATE Users
        SET user_points = user_points + ?
        WHERE user_id = ?
    ''', (_USER_ID, _NUM_POINTS))
    log_debug(f"Database UPDATE {_USER_ID} with {_NUM_POINTS} Points.")
    conn.commit()


def remove_points(_USER_ID, _NUM_POINTS):
    c.execute('''
        UPDATE Users
        SET user_points = user_points - ?
        WHERE user_id = ?
    ''', (_USER_ID, _NUM_POINTS))
    log_debug(f"Database UPDATE user: {_USER_ID} with -{_NUM_POINTS} Points.")
    conn.commit()


def see_points(_USER_ID):
    c.execute('''
        SELECT user_points 
        FROM Users
        WHERE user_id = ?
    ''', _USER_ID)
    data = c.fetchall()
    log_debug(f"Database SELECT user: {_USER_ID}.")
    return data


def see_top_10():
    c.execute('''
        SELECT user_id, user_points 
        FROM Users
        ORDER BY user_points DESC
        LIMIT 10
    ''')
    conn.commit()
    data = c.fetchall()
    log_debug(f"Database SELECT Top 10 users")
    return data


def see_user_data(_USER_ID):
    c.execute('''
        SELECT * 
        FROM Users
        WHERE user_id = ?
    ''', _USER_ID)
    data = c.fetchall()
    log_debug(f"Database SELECT all info from user: {_USER_ID}.")
    return data



