import discord
from discord.ext import commands
from __main__ import config

class admin_purge(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Removes up to 100 messages from channel.')
    @commands.has_permissions(manage_messages=True)
    @commands.has_role('Staff')
    async def purge_messages(self, ctx, number_messages: discord.Option(str)):

        # removes the need for a response
        await ctx.defer()
        logs_channel = await self.bot.fetch_channel(config['mod_log'])  # Welcome channel

        # Check that users are not removing from log channels
        if ctx.channel.id in logs_channel.values():
            await ctx.channel.send(f'{ctx.author.mention}, you should not be purging the {ctx.channel.mention}.')
            await logs_channel.send(f'{ctx.author.mention} atempted to purge the {ctx.channel.mention}.')
        else:
            # Do the purge
            await ctx.channel.purge(limit=int(number_messages))
            # Log the purge
            await logs_channel.send(
                f'{number_messages} messages purged from {ctx.channel.mention} by {ctx.author.mention}.')

    """
    Error handling
    """

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have the correct permissions to use this command!",
                reference=ctx.message)

        if isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must be a member of Staff to use this command!",
                                   reference=ctx.message)


def setup(bot):
    bot.add_cog(admin_purge(bot))
