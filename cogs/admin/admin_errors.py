from discord.ext import commands


class admin_errors(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Sends the last 100 lines of the error log.")
    @commands.has_permissions(manage_channels=True)
    async def show_error_log(self, ctx):
        with open('.\\utility\\testing.log', 'r') as logfile:
            logfile = logfile.read()

        await ctx.send(logfile[-2000:])


def setup(bot):
    bot.add_cog(admin_errors(bot))

