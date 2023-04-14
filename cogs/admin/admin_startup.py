from discord.ext import commands
from logs.logger import log_info
from cogs.utility._DB_create import create_db
import tomli


class onStartup(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log_info(" - Success.")
        with open("server.toml", "rb") as f:
            config = tomli.load(f)

        """
        Creates a User database and populates it with relevant info. 
        If a DB exists, it will simply connecty to that one.
        """
        create_db(self.bot, config['Database_name'], config['id'])
        log_info('\nBot is online and operational.')


def setup(bot):
    bot.add_cog(onStartup(bot))
