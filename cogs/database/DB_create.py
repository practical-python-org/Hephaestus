from discord.ext import commands
import sqlite3
import pandas as pd
from Hephaestus.logs.logger import log_info
from pathlib import Path
from __main__ import config


class database_innit(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Creates a new DB if one does not exist.')
    @commands.has_permissions(manage_messages=True)
    @commands.has_role('Owner')
    async def initialize_db(self, ctx):
        if not Path(config['Database_name']).is_file():
            conn = sqlite3.connect('Hephaestus.db')
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

            guild = self.bot.get_guild(config['id'])
            for member in guild.members:
                c.execute('''INSERT INTO Users (user_id, user_name, discriminator, nickname, user_roles_ids, 
                user_roles_names, top_role, avatar, joined_at, user_points, warnings) VALUES (?,?,?,?,?,?,?,?,?,?,?)''',
                          ((
                              member.id, member.display_name, member.discriminator, str(member.nick),
                              str([x.id for x in member.roles]), str([y.name for y in member.roles]),
                              member.top_role.id,
                              member.display_avatar.url, str(member.joined_at), 100, 0)
                          ))

            c.execute('''SELECT user_id, user_name, discriminator, nickname, user_roles_ids, user_roles_names, top_role, 
            avatar, joined_at, user_points, warnings FROM Users ''')

            log_info("Users successfully created. Printing results.")
            df = pd.DataFrame(c.fetchall(),
                              columns=['user_id', 'user_name', 'discriminator', 'nickname', 'user_roles_ids',
                                       'user_roles_names', 'top_role', 'avatar', 'joined_at', 'user_points',
                                       'warnings'])
            log_info(df.to_string())
            conn.commit()

            await ctx.channel.send("Database created.")
        else:
            await ctx.channel.send("Database already exists.")


def setup(bot):
    bot.add_cog(database_innit(bot))
