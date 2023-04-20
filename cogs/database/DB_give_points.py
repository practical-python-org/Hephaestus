import discord
from discord.ext import commands
from __main__ import config
from logs.logger import log_debug, log_info, log_critical
from cogs.utility._DB_Functions import give_points_to_user


class DB_give_points(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Give a user x amount of points.')
    @commands.has_role('Staff')
    async def give_points(self, ctx, amount_points, user: discord.User = None):
        guild = self.bot.get_guild(config['id'])
        member = guild.get_member(user.id)
        give_points_to_user(member.id, amount_points)

        message = f"{amount_points} Points given to {member} by {ctx.author}."
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
    bot.add_cog(DB_give_points(bot))
