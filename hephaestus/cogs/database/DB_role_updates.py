from discord.ext import commands
from cogs.utility._DB_Functions import update_roles
from logs.logger import log_debug


class DB_role_updates(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if len(before.roles) != len(after.roles):

            if after is None:
                member = before
            else:
                member = after

            ids = str([x.id for x in member.roles])
            names = str([y.name for y in member.roles])

            update_roles(member.id, ids, names)


def setup(bot):
    bot.add_cog(DB_role_updates(bot))
