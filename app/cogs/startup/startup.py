"""
Runs on the bot startup, handles creation/connection to the database.
"""
from discord.ext import commands
from logs.logger import *
from utility._db_create import create_db
import toml


class OnStartup(commands.Cog):
    """Uses a listener to init the DB"""
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        """Needs to load TOML to pull the DB name."""
        log_info(" - Success.")
        config = json.load(open('server.json'))
        create_db(self.bot, config['server_info']['database_name'], config['server_info']['id'])
        log_info(f"\nBot is online and using {config['server_info']['database_name']}")


def setup(bot):
    """ Adds the cog to the bot. """
    bot.add_cog(OnStartup(bot))
