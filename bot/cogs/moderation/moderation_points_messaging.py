"""
This grants +1 point every time a user sends a
message, and -1 point every time a user deletes a message.
"""
from discord.ext import commands
from bot.utility._db_functions import give_points_to_user, remove_points_from_user
from bot.logs.logger import log_debug


class ModerationPointsMessaging(commands.Cog):
    """
    Keep a balanced economy, it should.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        On every message, do things.
        Unless you are the bot listening.
        """
        if message.author != self.bot.user:
            log_debug(f'Point added to {message.author} for sending a message.')
            give_points_to_user(message.author.id, 1)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        On every message, do things.
        Unless you are the bot listening.
        """
        if message.author != self.bot.user:
            log_debug(f'Point removed from {message.author} for deleting a message.')
            remove_points_from_user(message.author.id, 1)


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(ModerationPointsMessaging(bot))
