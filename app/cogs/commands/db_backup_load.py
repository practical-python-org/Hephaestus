"""
This command works with db_backup to load a DB that has been copied to a home folder.
TODO: See if we can pull the 'config' out of here.
"""
import shutil
from pathlib import Path
from discord.ext import commands
from __main__ import config
from app.logs.logger import *


class DBbackupLoad(commands.Cog):
    """
    currently works by searching the home folder.
    -- Windows = 'C:/Users/username/hephaestus_backup'
    -- Unix = '/home/username/hephaestus_backup'
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Back up the DB.')
    @commands.has_role('Staff')
    async def load_db_backup(self, ctx):
        """
        Admin-level only.
        """
        if not ctx.author.guild_permissions.administrator:
            return ctx.channel.send("You dont have permission to load a backup DB.")
        # Assuming we have made a backup already in
        # Path.home() / "hephaestus_backup" / config['Database_name']
        src = Path.home() / "hephaestus_backup" / config['Database_name']
        dst = Path(__file__).parents[2] / config['Database_name']

        try:
            # Copy the file over to the destination
            shutil.copyfile(src, dst)
            log_info('Database restore successful')
            await ctx.respond('Database restore successful.')
        except OSError:
            log_info('Database restore failed. - No DB-backup found.')
            await ctx.respond(f'No DB found in {src}')

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """
        Handles any permissions errors for non-elevated users.
        """
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have the correct "
                "permissions to use this command!",
                reference=ctx.message)
        elif isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must be a member "
                                   "of Staff to use this command!",
                                   reference=ctx.message)
        else:
            raise error


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(DBbackupLoad(bot))
