"""
This command allows an elevated user to quickly check the logs for errors.
Log level can be adjusted in /bot/logs/logger.py
TODO: Check if we can add some logic to send more than 100 lines of the log.
      We are only limited here by the size of the embed field (2000 chars).
TODO: See if we can pull the 'config' out of here. why not hardcode the name?
"""
import pathlib
from discord.ext import commands
from __main__ import config


class AdminErrors(commands.Cog):
    """
    Simply reads out the log file stored in bot/logs/*.log
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Sends the last 100 lines of the error log.")
    @commands.has_role('Staff')
    async def show_error_log(self, ctx):
        """
        Uses pathlib to send 2000 lines of the error log.
        """
        log_file_path = pathlib.Path('logs', config['logFileName'])
        with open(log_file_path, 'r', encoding='UTF-8') as logfile:
            logfile = logfile.read()
        await ctx.respond(f"```bash\n{logfile[-1970:]}\n```")

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """
        Handles any permissions errors for non-elevated users.
        """
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have "
                "the correct permissions to use this command!",
                reference=ctx.message)
        elif isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must be "
                                   "a member of Staff to use this command!",
                                   reference=ctx.message)
        else:
            raise error


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(AdminErrors(bot))
