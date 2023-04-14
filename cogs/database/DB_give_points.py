import discord
from discord.ext import commands
from __main__ import config
from logs.logger import log_debug, log_info, log_critical
from cogs.utility._DB_Functions import give_points_to_user


class DB_give_points(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Give a user x amount of points.')
    async def give_points(self, ctx, amount_points, user: discord.User = None):
        guild = self.bot.get_guild(config['id'])
        member = guild.get_member(user.id)
        give_points_to_user(member.id, amount_points)

        message = f"{amount_points} Points given to {member} by {ctx.author}."
        log_info(message)
        await ctx.respond(message)


def setup(bot):
    bot.add_cog(DB_give_points(bot))
