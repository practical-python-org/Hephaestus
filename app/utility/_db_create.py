"""
Handles creation and initialization of the DB
Is only called in the OnStartup function at app/cogs/startup/startup.py
"""
import os
from pathlib import Path
import sqlite3
import pandas as pd
from logs.logger import *


def create_db(discord_client, db_name, guild_id):
    """
    DB_PATH = Path(f'/app/db/{DB_NAME}')
    Cross platform way of init-ing a DB
    """
    db_path = ((Path.cwd() / db_name) if os.name == 'nt' else Path(f'/app/db/{db_name}'))
    log_info('Loading Database...')

    if db_path.exists() is False:
        conn = sqlite3.connect(db_path)
        connection = conn.cursor()
        log_info(" - No DB detected - Creating Database...")
        connection.execute('''
                  CREATE TABLE IF NOT EXISTS Users
                  ([user_id] INTEGER PRIMARY KEY NOT NULL,
                   [user_name] TEXT,
                   [discriminator] TEXT,
                   [nickname] TEXT,
                   [user_roles_ids] TEXT,
                   [user_roles_names] TEXT,
                   [top_role] TEXT,
                   [avatar] TEXT,
                   [joined_at] TEXT,
                   [user_points] INTEGER,
                   [warnings] INTEGER
                   )
                  ''')
        log_info(" - Database Created. Populating Users table...")

        guild = discord_client.get_guild(guild_id)
        for member in guild.members:
            connection.execute('''INSERT INTO Users
                     (user_id, user_name, discriminator, nickname, user_roles_ids, 
                     user_roles_names, top_role, avatar, joined_at, user_points, warnings)
                     VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                               ((
                                   member.id
                                   , member.display_name
                                   , member.discriminator
                                   , str(member.nick)
                                   , str([x.id for x in member.roles])
                                   , str([y.name for y in member.roles])
                                   , member.top_role.id
                                   , member.display_avatar.url
                                   , str(member.joined_at)
                                   , 100
                                   , 0
                               )
                               ))

        conn.commit()
        connection.close()
        log_info(" - Success.")

    else:
        conn = sqlite3.connect(db_path)
        connection = conn.cursor()
        connection.execute('''SELECT
                    user_id, user_name, discriminator, nickname,
                    user_roles_ids, user_roles_names, top_role,
                    avatar, joined_at, user_points, warnings
                    FROM Users''')
        conn.commit()

        dataframe = pd.DataFrame(
            connection.fetchall(),
            columns=['user_id', 'user_name', 'discriminator'
                , 'nickname', 'user_roles_ids', 'user_roles_names'
                , 'top_role', 'avatar', 'joined_at'
                , 'user_points', 'warnings'])
        log_debug(dataframe.to_string())
        connection.close()
        log_info(" - Success.")
