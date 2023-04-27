import discord
from discord.ext import commands
from discord import option
from __main__ import config
from logs.logger import log_debug, log_info, log_critical
from utility._db_functions import remove_points_from_user


class DB_remove_points(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Remove x amount of points from user.')
    @option("amount_points"
            , description="Enter an amount between 1 and 20."
            , min_value=1
            , max_value=20
            , required=True
            )
    @option("user"
            , description="Enter a user."
            , required=True
            )
    @commands.has_role('Staff')
    async def remove_points(self
                            , ctx: discord.ApplicationContext
                            , amount_points: int
                            , user: discord.User
                            ):

        guild = self.bot.get_guild(config['id'])
        member = guild.get_member(user.id)
        remove_points_from_user(user.id, amount_points)

        message = f"{amount_points} Points removed from {member} by {ctx.author}."
        log_info(message)
        await ctx.respond(message)

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have the correct permissions to use this command!",
                reference=ctx.message)
        elif isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must be a member of Staff to use this command!",
                                   reference=ctx.message)
        else:
            raise error


def setup(bot):
    bot.add_cog(DB_remove_points(bot))
