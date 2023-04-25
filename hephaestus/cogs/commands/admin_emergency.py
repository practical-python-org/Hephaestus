from discord.ext import commands

from hephaestus.logs.logger import log_info


class admin_emergency(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="Removes all permissions from everyone in the server except the staff.")
    @commands.has_role("Staff")
    async def lockdown(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            return ctx.channel.send("You dont have permission to run a lockdown.")
        log_info("Initiated a lockdown.")
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
                await channel.send(channel.mention + " ***is now in lockdown.***")

    @commands.slash_command(description="Reinstates all permissions to everyone in the server.")
    @commands.has_role("Staff")
    async def unlock(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            return ctx.channel.send("You dont have permission to lift a lockdown.")
        log_info("Releasing lockdown.")
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                await channel.set_permissions(ctx.guild.default_role, send_messages=None)
                await channel.send(channel.mention + " ***has been unlocked.***")

    async def cog_command_error(self, ctx: commands.Context, error: commands.CommandError):
        if isinstance(error, commands.MissingPermissions):
            await ctx.channel.send(
                f"Sorry, {ctx.author.name}, you dont have the correct permissions to use this command!", reference=ctx.message
            )
        elif isinstance(error, commands.MissingRole):
            await ctx.channel.send(f"Sorry, {ctx.author.name}, you must be a member of Staff to use this command!", reference=ctx.message)
        else:
            raise error


def setup(bot):
    bot.add_cog(admin_emergency(bot))
