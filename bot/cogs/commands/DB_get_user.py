import discord
from discord.ext import commands
from discord import option
from __main__ import config
from logs.logger import log_debug, log_info, log_critical
from utility._db_functions import see_user_data
from utility._embeds import embed_user_profile


class DB_get_user(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='See a profile of information on a user.')
    @option("user"
            , description="Enter a user."
            , required=True
            )
    async def get_user(self
                       , ctx: discord.ApplicationContext
                       , user: discord.User
                       ):
        guild = self.bot.get_guild(config['id'])
        member = guild.get_member(user.id)

        profile = see_user_data(member.id)
        log_info(f"Data on {member} requested by {ctx.author}.")
        log_info(profile)
        embed = embed_user_profile(profile)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(DB_get_user(bot))
