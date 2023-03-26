import sqlite3
from Hephaestus.logs.logger import log_info, log_critical
from __main__ import config


def give_points(_USER_ID, _NUM_POINTS):
    conn = sqlite3.connect(config['Database_name'])
    c = conn.cursor()
    c.execute('''
        UPDATE Users
        SET user_points = user_points + ?
        WHERE user_id = ?
    ''', (_USER_ID, _NUM_POINTS))
    conn.commit()


def remove_points(_USER_ID, _NUM_POINTS):
    conn = sqlite3.connect(config['Database_name'])
    c = conn.cursor()
    c.execute('''
        UPDATE Users
        SET user_points = user_points - ?
        WHERE user_id = ?
    ''', (_USER_ID, _NUM_POINTS))
    conn.commit()


def see_points(_USER_ID):
    conn = sqlite3.connect(config['Database_name'])
    c = conn.cursor()
    c.execute('''
        SELECT user_points 
        FROM Users
        WHERE user_id = ?
    ''', (_USER_ID))
    data = c.fetchall()
    return data


def see_top_10():
    conn = sqlite3.connect(config['Database_name'])
    c = conn.cursor()
    c.execute('''
        SELECT user_id, user_points 
        FROM Users
        ORDER BY user_points DESC
        LIMIT 10
    ''')
    data = c.fetchall()
    return data

def see_user_data(_USER_ID):
    conn = sqlite3.connect(config['Database_name'])
    c = conn.cursor()
    c.execute('''
        SELECT * 
        FROM Users
        WHERE user_id = ?
    ''', (_USER_ID))
    data = c.fetchall()
    return data



