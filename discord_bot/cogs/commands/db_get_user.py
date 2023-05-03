"""
This command grabs info from a user, sends it to discord_bot/utility/_embeds
and then produces a report on the user as a bot response.
TODO: Pull the config out of here. We should be able to use ctx.guild.id, and
      then move into fetch_member() from there.
"""
import discord
from discord.ext import commands
from discord import option  # py-cord ONLY
from __main__ import config
from discord_bot.logs.logger import *
from discord_bot.utility._db_functions import see_user_data
from discord_bot.utility._embeds import embed_user_profile


class DBgetUser(commands.Cog):
    """
    Directly sends a query to our DB using Fn see_user_data(),
    located in discord_bot/utility/_db_functions
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='See a profile of information on a user.')
    @option("user"
            , description="Enter a user."
            , required=True
            )
    async def get_user(self, ctx: discord.ApplicationContext, user: discord.User):
        """
        First gets the guild ID, then the member ID from that, and then
        queries the db to get the relevant data.
        """
        guild = self.bot.get_guild(config['id'])
        member = guild.get_member(user.id)

        profile = see_user_data(member.id)
        log_info(f"Data on {member} requested by {ctx.author}.")
        log_info(profile)
        embed = embed_user_profile(profile)

        await ctx.respond(embed=embed)


def setup(bot):
    """
    Necessary for loading the cog into the discord_bot instance.
    """
    bot.add_cog(DBgetUser(bot))
