import shutil
from pathlib import Path
from discord.ext import commands
from __main__ import config
from logs.logger import log_info


class DBbackup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Back up the DB.')
    @commands.has_role('Staff')
    async def backup_db(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            return ctx.channel.send("You dont have permission to back up the DB.")
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

        await ctx.respond('Database backup successful.')

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have the correct \
                permissions to use this command!",
                reference=ctx.message)
        elif isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must \
             be a member of Staff to use this command!",
                                   reference=ctx.message)
        else:
            raise error


def setup(bot):
    bot.add_cog(DBbackup(bot))
