from discord.ext import commands
import pathlib
from __main__ import config


class admin_errors(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Sends the last 100 lines of the error log.")
    @commands.has_permissions(manage_channels=True)
    async def show_error_log(self, ctx):
        log_file_path = pathlib.Path('logs', config['logFileName'])
        with open(log_file_path, 'r') as logfile:
            logfile = logfile.read()

        await ctx.send(f"```bash\n{logfile[-1970:]}\n```")  # Format the error log in a code block.


def setup(bot):
    bot.add_cog(admin_errors(bot))

