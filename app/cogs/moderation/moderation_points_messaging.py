"""
This grants +1 point every time a user sends a
message, and -1 point every time a user deletes a message.
"""
from discord.ext import commands
from utility._db_functions import give_points_to_user, remove_points_from_user
from logs.logger import *


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
            points_for_message = len(message.content.split(' '))
            log_debug(f'{points_for_message} points added to {message.author} for sending a message.')
            give_points_to_user(message.author.id, points_for_message)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        On every message, do things.
        Unless you are the bot listening.
        """
        if message.author != self.bot.user:
            points_for_message = len(message.content.split(' '))
            log_debug(f'{points_for_message} points removed from {message.author} for deleting a message.')
            remove_points_from_user(message.author.id, points_for_message)


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(ModerationPointsMessaging(bot))
