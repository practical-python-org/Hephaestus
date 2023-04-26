import discord
from discord.ext import commands
from __main__ import config
from logs.logger import log_info
from utility._embeds import embed_unban


class logging_unbans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_unban(self, guild, member: discord.Member):
        embed = embed_unban(member)

        log_info(f"{member.name} was unbanned. Welcome back.")
        logs_channel = await self.bot.fetch_channel(config['mod_log'])  # Welcome channel
        await logs_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(logging_unbans(bot))
