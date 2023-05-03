"""
This listens for role updates and queries the DB with the new role set
"""
from discord.ext import commands
from utility._db_functions import update_roles
from logs.logger import log_debug


class DBRoleUpdates(commands.Cog):
    """
    Necessary because the get_user() command was not updating.
    This cog keeps the DB updated with current info.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        """
        'before' and 'after' are discord.member objects.
        """
        if len(before.roles) != len(after.roles):

            if after is None:
                member = before
            else:
                member = after

            ids = str([x.id for x in member.roles])
            names = str([y.name for y in member.roles])

            log_debug(f"Updating roles for {member.name}")
            update_roles(member.id, ids, names)


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(DBRoleUpdates(bot))
