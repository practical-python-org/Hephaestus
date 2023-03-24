import discord
from discord.ext import commands
from datetime import datetime
from __main__ import config
from Hephaestus.logs.logger import log_info


class logging_avatars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        if before.avatar != after.avatar:
            embed = discord.Embed(title=f'{before} updated their profile picture!'
                                  , color=discord.Color.dark_grey()
                                  , timestamp=datetime.utcnow())
            embed.set_thumbnail(url=after.avatar)

            log_info(f"{before} changed their avatar.")
            logs_channel = await self.bot.fetch_channel(config['user_log'])
            await logs_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(logging_avatars(bot))
