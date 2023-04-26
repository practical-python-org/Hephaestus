from discord.ext import commands
from __main__ import config
from logs.logger import log_info
from utility._embeds import embed_avatar


class logging_avatars(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_user_update(self, before, after):
        if before.avatar != after.avatar:
            embed = embed_avatar(before, after)

            log_info(f"{before} changed their avatar.")

            logs_channel = await self.bot.fetch_channel(config['mod_log'])
            await logs_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(logging_avatars(bot))
