from discord.ext import commands
from pathlib import Path
from __main__ import config
import shutil
from logs.logger import log_debug, log_info, log_critical


class DB_backup(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Back up the DB.')
    async def backup_db(self, ctx):
        # Location of current DB
        src = Path(__file__).parents[2] / config['Database_name']

        # Destination of Backup
        # -- Windows = 'C:/Users/username/hephaestus_backup'
        # -- Unix = '/home/username/hephaestus_backup'
        dst = Path.home() / "hephaestus_backup"
        # Make dir if it does not exist
        dst.mkdir(parents=True, exist_ok=True)
        dst = dst / config['Database_name']
        log_info(f'Backing up Database to: {dst}')

        # Copy the file over to the destination
        shutil.copyfile(src, dst)

        await ctx.respond(f'Database backup successful.')


def setup(bot):
    bot.add_cog(DB_backup(bot))
