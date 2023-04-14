from discord.ext import commands
from logs.logger import log_info


class admin_emergency(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description="For debugging. Displays the channels of a guild within the terminal.")
    @commands.has_permissions(manage_channels=True)
    async def channels(self, ctx):
        text_channel_list = []
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                text_channel_list.append(channel)
        log_info(text_channel_list)
        await ctx.send('printed in terminal')

    @commands.slash_command(description="Removes all permissions from everyone in the server except the staff.")
    @commands.has_permissions(manage_channels=True)
    async def lockdown(self, ctx):
        log_info("Initiated a lockdown.")
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                await channel.set_permissions(ctx.guild.default_role, send_messages=False)
                await channel.send(channel.mention + " ***is now in lockdown.***")

    @commands.slash_command(description="Reinstates all permissions to everyone in the server.")
    @commands.has_permissions(manage_channels=True)
    async def unlock(self, ctx):
        log_info("Releasing lockdown.")
        for guild in self.bot.guilds:
            for channel in guild.text_channels:
                await channel.set_permissions(ctx.guild.default_role, send_messages=None)
                await channel.send(channel.mention + " ***has been unlocked.***")


def setup(bot):
    bot.add_cog(admin_emergency(bot))


