import discord
from discord.ext import commands
from datetime import datetime
from __main__ import config
from Hephaestus.logs.logger import log_info


class logging_unbans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member: discord.Member):
        embed = discord.Embed(title=f'<:green_circle:1046088647759372388> User Un-Banned'
                              , color=discord.Color.red()
                              , timestamp=datetime.utcnow())

        embed.add_field(name=f'{member.name} was un-banned.'
                        , value='Welcome back.'
                        , inline=True)

        log_info(f"{member.name} was unbanned. Welcome back.")
        logs_channel = await self.bot.fetch_channel(config['mod_log'])  # Welcome channel
        await logs_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(logging_unbans(bot))
