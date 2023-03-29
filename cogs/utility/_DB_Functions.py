import sqlite3
from pathlib import Path
from Hephaestus.logs.logger import log_debug, log_info, log_critical
from __main__ import config

DB_PATH = (Path.cwd() / config["Database_name"])



def give_points(_USER_ID, _NUM_POINTS):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        UPDATE Users
        SET user_points = user_points + ?
        WHERE user_id = ?
    ''', (_USER_ID, _NUM_POINTS))
    log_debug(f"Database UPDATE {_USER_ID} with {_NUM_POINTS} Points.")
    conn.commit()


def remove_points(_USER_ID, _NUM_POINTS):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        UPDATE Users
        SET user_points = user_points - ?
        WHERE user_id = ?
    ''', (_USER_ID, _NUM_POINTS))
    log_debug(f"Database UPDATE user: {_USER_ID} with -{_NUM_POINTS} Points.")
    conn.commit()


def see_points(_USER_ID):
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute('''
        SELECT user_points 
        FROM Users
        WHERE user_id = ?
    ''', _USER_ID)
    data = c.fetchall()
    log_debug(f"Database SELECT user: {_USER_ID}.")
    return data


def see_top_10():
    log_info(DB_PATH)
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
    ''', _USER_ID)
    data = c.fetchall()

    conn.commit()  # need at least 1 commit
    c.close()
    log_debug(f"Database SELECT all info from user: {_USER_ID}.")
    return data
