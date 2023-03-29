import sqlite3
from Hephaestus.logs.logger import log_info, log_debug
from pathlib import Path
import pandas as pd


def create_db(DISCORD_CLIENT, DB_NAME, GUILD_ID):
    DB_PATH = (Path.cwd() / DB_NAME)

    if DB_PATH.exists() is False:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        log_info("Creating Database...")
        c.execute('''
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
        log_info("Database Created. Populating Users table...")

        guild = DISCORD_CLIENT.get_guild(GUILD_ID)
        for member in guild.members:
            c.execute('''INSERT INTO Users (user_id, user_name, discriminator, nickname, user_roles_ids, 
            user_roles_names, top_role, avatar, joined_at, user_points, warnings) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                      ((
                          member.id, member.display_name, member.discriminator, str(member.nick),
                          str([x.id for x in member.roles]), str([y.name for y in member.roles]),
                          member.top_role.id,
                          member.display_avatar.url, str(member.joined_at), 100, 0)
                      ))

        c.close()
        conn.commit()  # need at least 1 commit
        c.close()
        log_info("Database successfully created.")

    else:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        c.execute('''SELECT user_id, user_name, discriminator, nickname, user_roles_ids, user_roles_names, top_role,
        avatar, joined_at, user_points, warnings FROM Users''')
        conn.commit()

        df = pd.DataFrame(c.fetchall(),
                          columns=['user_id', 'user_name', 'discriminator', 'nickname', 'user_roles_ids',
                                   'user_roles_names', 'top_role', 'avatar', 'joined_at', 'user_points',
                                   'warnings'])
        log_debug(df.to_string())
        log_info("Database already exists and contains data.")
