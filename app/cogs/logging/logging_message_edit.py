"""
Logs messages that get edited.
"""
from discord.ext import commands
from __main__ import config
from logs.logger import *
from utility._embeds import embed_message_edit


class LoggingMessageEdit(commands.Cog):
    """
    Simple listener to on_message_edit
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_edit(self, message_before, message_after):
        """
        Just checking if the content before is != to the content after.
        """
        if message_before.content != message_after.content:

            if message_before.author.nick is None:
                username = message_before.author
            else:
                username = message_before.author.nick

            author = message_before.author
            embed = embed_message_edit(username, author, message_before, message_after)

            logs_channel = await self.bot.fetch_channel(config['server_channels']['mod_log'])
            log_info(f"{author} edited a message.")
            await logs_channel.send(embed=embed)


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(LoggingMessageEdit(bot))
