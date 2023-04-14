import discord
from discord.ext import commands
from __main__ import config
from logs.logger import log_debug, log_info, log_critical
from cogs.utility._DB_Functions import remove_points_from_user


class DB_remove_points(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Remove x amount of points from user.')
    async def remove_points(self, ctx, amount_points, user: discord.User = None):
        guild = self.bot.get_guild(config['id'])
        member = guild.get_member(user.id)
        remove_points_from_user(user.id, amount_points)

        message = f"{amount_points} Points removed from {member} by {ctx.author}."
        log_info(message)
        await ctx.respond(message)


def setup(bot):
    bot.add_cog(DB_remove_points(bot))
