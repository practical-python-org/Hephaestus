"""
Logs name changes.
TODO: Pull config out of here.
"""
from discord.ext import commands
from __main__ import config
from discord_bot.logs.logger import *
from discord_bot.utility._embeds import embed_name_change


class LoggingNameChanges(commands.Cog):
    """
    Simple listener to on_member_update
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """
        Just checking if the name before is != to the name after.
        """
        if before.nick is None:
            username_before = before
        else:
            username_before = before.nick

        if after.nick is None:
            username_after = after
        else:
            username_after = after.nick

        if before.nick != after.nick and before.nick is not None:
            embed = embed_name_change(before, after, username_before, username_after)

            log_info(f"{username_before} has changed their name to {username_after}.")
            logs_channel = await self.bot.fetch_channel(config['mod_log'])
            await logs_channel.send(f'{username_after.mention}', embed=embed)


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(LoggingNameChanges(bot))
