import sqlite3
from pathlib import Path
from logs.logger import log_debug, log_info, log_critical
from __main__ import config


DB_PATH = Path(f'/database/{config["Database_name"]}')
# DB_PATH = (Path.cwd() / config["Database_name"])


def see_top_10():
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''SELECT user_id, user_points 
        FROM Users
        ORDER BY user_points DESC
        LIMIT 10
    ''')
    data = c.fetchall()
    conn.commit()  # need at least 1 commit
    c.close()
    log_debug(f"Database SELECT Top 10 users")
    return data


def see_user_data(_USER_ID):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT * 
        FROM Users
        WHERE user_id = ?
    ''', (_USER_ID, ))
    data = c.fetchall()
    conn.commit()  # need at least 1 commit
    c.close()
    log_debug(f"Database SELECT all info from user: {_USER_ID}.")
    return data


def give_points_to_user(_USER_ID, _NUM_POINTS):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        UPDATE Users
        SET user_points = user_points + ?
        WHERE user_id = ?
    ''', (_NUM_POINTS, _USER_ID))
    log_debug(f"Database UPDATE {_USER_ID} with {_NUM_POINTS} Points.")
    conn.commit()
    c.close()
    return


def remove_points_from_user(_USER_ID, _NUM_POINTS):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        UPDATE Users
        SET user_points = user_points - ?
        WHERE user_id = ?
    ''', (_NUM_POINTS, _USER_ID))
    log_debug(f"Database UPDATE {_USER_ID} with -{_NUM_POINTS} Points.")
    conn.commit()
    c.close()
    return


def see_points(_USER_ID):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT user_points 
        FROM Users
        WHERE user_id = ?
    ''', _USER_ID)
    data = c.fetchall()
    conn.commit()  # need at least 1 commit
    c.close()
    log_debug(f"Database SELECT user: {_USER_ID}.")
    return data
