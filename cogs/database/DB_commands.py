from discord.ext import commands
import sqlite3
import pandas as pd

from Hephaestus.cogs.database import _DB_Functions
from Hephaestus.logs.logger import log_info
from pathlib import Path
from __main__ import config

import discord
from discord.ext import commands
from __main__ import config
from Hephaestus.logs.logger import log_info
import Hephaestus.cogs.database._DB_Functions as DB


class db_commands(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='See the top 10 point earners.')
    async def leaderboard(self, ctx):
        data = DB.see_top_10()
        log_info(data)
        guild = self.bot.get_guild(config['id'])
        for person in data:
            member_id = person[0]
            member = guild.get_member(member_id)
            print(f"{member.display_name} - {person[1]}")
              # TODO: build embed, make pretty.
        await ctx.channel.send("cool")

def setup(bot):
    bot.add_cog(db_commands(bot))
