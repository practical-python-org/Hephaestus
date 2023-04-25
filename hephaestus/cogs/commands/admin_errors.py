import pathlib

from discord.ext import commands

from hephaestus.__main__ import config


class admin_errors(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Sends the last 100 lines of the error log.")
    @commands.has_role("Staff")
    async def show_error_log(self, ctx):
        log_file_path = pathlib.Path("logs", config["logFileName"])
        with open(log_file_path, "r") as logfile:
            logfile = logfile.read()
        await ctx.respond(f"```bash\n{logfile[-1970:]}\n```")  # Format the error log in a code block.

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have the correct permissions to use this command!", reference=ctx.message
            )
        elif isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must be a member of Staff to use this command!", reference=ctx.message)
        else:
            raise error


def setup(bot):
    bot.add_cog(admin_errors(bot))
