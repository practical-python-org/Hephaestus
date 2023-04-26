import discord
from discord import option
from discord.ext import commands

from hephaestus.__main__ import config
from hephaestus.cogs.utility._DB_Functions import see_user_data
from hephaestus.cogs.utility._embeds import embed_user_profile
from hephaestus.logs.logger import log_critical, log_debug, log_info


class DB_get_user(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="See a profile of information on a user.")
    @option("user", description="Enter a user.", required=True)
    async def get_user(self, ctx: discord.ApplicationContext, user: discord.User):
        guild = self.bot.get_guild(config["id"])
        member = guild.get_member(user.id)

        profile = see_user_data(member.id)
        log_info(f"Data on {member} requested by {ctx.author}.")
        log_info(profile)
        embed = embed_user_profile(profile)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(DB_get_user(bot))