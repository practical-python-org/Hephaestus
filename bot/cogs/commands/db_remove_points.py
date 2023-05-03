"""
This command takes an amount of points and a user and
updates the DB with the new total points.
TODO: Pull the config out of here. We should be able to use ctx.guild.id, and
      then move into fetch_member() from there.
"""
import discord
from discord.ext import commands
from discord import option  # Py-cord ONLY
from __main__ import config
from logs.logger import log_info
from utility._db_functions import remove_points_from_user


class DBRemovePoints(commands.Cog):
    """
    Staff only command to remove points from a user. min/max = 1/20.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Remove x amount of points from user.')
    @option("amount_points"
        , description="Enter an amount between 1 and 20."
        , min_value=1
        , max_value=20
        , required=True
            )
    @option("user", description="Enter a user.", required=True)
    @commands.has_role('Staff')
    async def remove_points(self
                            , ctx: discord.ApplicationContext
                            , amount_points: int
                            , user: discord.User
                            ):
        """
        First gets the guild ID, then the member ID from that, and then
        queries the db to update the relevant data.
        """
        guild = self.bot.get_guild(config['id'])
        member = guild.get_member(user.id)
        remove_points_from_user(user.id, amount_points)

        message = f"{amount_points} Points removed from {member} by {ctx.author}."
        log_info(message)
        await ctx.respond(message)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        """
        Handles any permissions errors for non-elevated users.
        """
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have the correct "
                "permissions to use this command!",
                reference=ctx.message)
        elif isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must be a "
                                   "member of Staff to use this command!",
                                   reference=ctx.message)
        else:
            raise error


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(DBRemovePoints(bot))
