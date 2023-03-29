import discord
from discord.ext import commands
from __main__ import config
from Hephaestus.logs.logger import log_debug, log_info, log_critical
from Hephaestus.cogs.utility._DB_Functions import see_user_data
from Hephaestus.cogs.utility._embeds import embed_leaderboard


class DB_get_user(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='See a profile of information on a user.')
    async def get_info_for_user(self, ctx, user: discord.User=None):
        guild = self.bot.get_guild(config['id'])
        member = guild.get_member(user.id)
        profile = see_user_data(member)
        log_info(profile)




def setup(bot):
    bot.add_cog(DB_get_user(bot))