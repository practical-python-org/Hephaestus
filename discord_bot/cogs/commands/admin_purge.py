"""
This is a user command that removes x amount of messages from a channel.
TODO: See if we can pull the 'config' out of here.
"""
from discord.ext import commands
from discord import option
from __main__ import config
from discord_bot.logs.logger import *


class AdminPurge(commands.Cog, command_attrs=dict(hidden=True)):
    """
    The purge command uses ctx.channel.purge to remove messages.
    It is limited to 100 messages.
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Removes up to 100 messages from channel.')
    @commands.has_permissions(manage_messages=True)
    @commands.has_role('Staff')
    @option("number_messages"
            , description="Enter an amount between 1 and 100."
            , min_value=1
            , max_value=100
            , required=True
            )
    async def purge_messages(self, ctx, number_messages: int):
        """
        Make sure to log the purge, so that it can be examined in the case of a discrepancy.
        """
        logs_channel = await self.bot.fetch_channel(config['mod_log'])

        # Do the purge
        await ctx.channel.purge(limit=int(number_messages))

        # Log the purge
        log_info(f"{ctx.author} purged {number_messages} messages from {ctx.channel}.")
        await logs_channel.send(
            f'{number_messages} messages purged '
            'from {ctx.channel.mention} by {ctx.author.mention}.')

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
    bot.add_cog(AdminPurge(bot))
