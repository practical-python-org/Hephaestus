from discord.ext import commands

from hephaestus.cogs.utility._DB_Functions import (
    give_points_to_user,
    remove_points_from_user,
)
from hephaestus.logs.logger import log_debug


class moderation_points_messaging(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        else:
            log_debug(f"Point added to {message.author} for sending a message.")
            give_points_to_user(message.author.id, 1)

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        if message.author == self.bot.user:
            return
        else:
            log_debug(f"Point removed from {message.author} for deleting a message.")
            remove_points_from_user(message.author.id, 1)


def setup(bot):
    bot.add_cog(moderation_points_messaging(bot))
