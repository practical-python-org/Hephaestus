from discord.ext import commands
from utility.logger import log


class onStartup(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log('Bot is online and operational.')


def setup(bot):
    bot.add_cog(onStartup(bot))
