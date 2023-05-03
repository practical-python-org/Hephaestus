"""
Logs avatar changes
TODO: Pull config out of here.
"""
from discord.ext import commands
from __main__ import config
from discord_bot.logs.logger import *
from discord_bot.utility._embeds import embed_avatar


class LoggingAvatars(commands.Cog):
    """
    Simple listener to on_user_update
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        """
        if the avatar before is != to the avatar after, do stuff.
        """
        if before.avatar != after.avatar:
            embed = embed_avatar(before, after)

            log_info(f"{before} changed their avatar.")

            logs_channel = await self.bot.fetch_channel(config['mod_log'])
            await logs_channel.send(embed=embed)


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(LoggingAvatars(bot))
