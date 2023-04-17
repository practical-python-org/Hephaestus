from discord.ext import commands
from pathlib import Path
from __main__ import config
import shutil
from logs.logger import log_debug, log_info, log_critical


class DB_backup_load(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Back up the DB.')
    async def load_db_backup(self, ctx):
        # Assuming we have made a backup already in Path.home() / "hephaestus_backup" / config['Database_name']
        src = Path.home() / "hephaestus_backup" / config['Database_name']
        dst = Path(__file__).parents[2] / config['Database_name']

        try:
            # Copy the file over to the destination
            shutil.copyfile(src, dst)

            await ctx.respond(f'Database restore successful.')
        except:
            await ctx.respond(f'No DB found in {src}')


def setup(bot):
    bot.add_cog(DB_backup_load(bot))
