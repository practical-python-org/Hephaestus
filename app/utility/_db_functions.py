"""
This file supports the application by functionizing
important database i/o queries.
TODO: See if we can import the DB name without the TOML file.
"""
import os
import sqlite3
from pathlib import Path
from logs.logger import *
from __main__ import config

db_path = ((Path.cwd() / config["Database_name"])
           if os.name == 'nt'
           else Path(f'/app/db/{config["Database_name"]}'))


def see_top_10():
    """
    Grabs the top 10 point earners in the DB
    """
    conn = sqlite3.connect(db_path)
    connection = conn.cursor()
    connection.execute('''SELECT user_id, user_points
        FROM Users
        ORDER BY user_points DESC
        LIMIT 10
    ''')
    data = connection.fetchall()
    conn.commit()  # need at least 1 commit
    connection.close()
    log_debug("Database SELECT Top 10 users")
    return data


def see_user_data(user_id):
    """
    Grabs user data for the specified user
    """
    conn = sqlite3.connect(db_path)
    connection = conn.cursor()
    connection.execute('''
        SELECT * 
        FROM Users
        WHERE user_id = ?
    ''', (user_id,))
    data = connection.fetchall()
    conn.commit()  # need at least 1 commit
    connection.close()
    log_debug(f"Database SELECT all info from user: {user_id}.")
    return data


def give_points_to_user(user_id, num_points):
    """
    Gives x amount of points to the specified user
    """
    conn = sqlite3.connect(db_path)
    connection = conn.cursor()
    connection.execute('''
        UPDATE Users
        SET user_points = user_points + ?
        WHERE user_id = ?
    ''', (num_points, user_id))
    log_debug(f"Database UPDATE {user_id} with {num_points} Points.")
    conn.commit()
    connection.close()


def remove_points_from_user(user_id, num_points):
    """
    Removes x amount of points from the specified user
    """
    conn = sqlite3.connect(db_path)
    connection = conn.cursor()
    connection.execute('''
        UPDATE Users
        SET user_points = user_points - ?
        WHERE user_id = ?
    ''', (num_points, user_id))
    log_debug(f"Database UPDATE {user_id} with -{num_points} Points.")
    conn.commit()
    connection.close()


def see_points(user_id):
    """
    Checks the amount of points the specified user has
    """
    conn = sqlite3.connect(db_path)
    connection = conn.cursor()
    connection.execute('''
        SELECT user_points 
        FROM Users
        WHERE user_id = ?
    ''', user_id)
    data = connection.fetchall()
    conn.commit()  # need at least 1 commit
    connection.close()
    log_debug(f"Database SELECT POINTS user: {user_id}.")
    return data


def update_roles(user_id, role_ids, role_names):
    """
    Updates the DB with a specific users current roles.
    """
    conn = sqlite3.connect(db_path)
    connection = conn.cursor()
    connection.execute('''
        UPDATE Users
        SET user_roles_ids = ?
        , user_roles_names = ?
        WHERE user_id = ?
    ''', (role_ids, role_names, str(user_id)))
    data = connection.fetchall()
    conn.commit()  # need at least 1 commit
    connection.close()
    log_debug(f"Database UPDATE ROLES for user: {user_id}.")
    return data
