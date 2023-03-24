from discord.ext import commands
from Hephaestus.logs.logger import log_info


class onStartup(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        log_info('Bot is online and operational.')


def setup(bot):
    bot.add_cog(onStartup(bot))
