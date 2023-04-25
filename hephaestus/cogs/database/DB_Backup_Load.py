from discord.ext import commands
from pathlib import Path
from __main__ import config
import shutil
from logs.logger import log_debug, log_info, log_critical


class DB_backup_load(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Back up the DB.')
    @commands.has_role('Staff')
    async def load_db_backup(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            return ctx.channel.send("You dont have permission to load a backup DB.")
        # Assuming we have made a backup already in Path.home() / "hephaestus_backup" / config['Database_name']
        src = Path.home() / "hephaestus_backup" / config['Database_name']
        dst = Path(__file__).parents[2] / config['Database_name']

        try:
            # Copy the file over to the destination
            shutil.copyfile(src, dst)

            await ctx.respond(f'Database restore successful.')
        except:
            await ctx.respond(f'No DB found in {src}')

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have the correct permissions to use this command!",
                reference=ctx.message)
        elif isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must be a member of Staff to use this command!",
                                   reference=ctx.message)
        else:
            raise error


def setup(bot):
    bot.add_cog(DB_backup_load(bot))
