from discord.ext import commands
from __main__ import config
from logs.logger import log_info
from cogs.utility._embeds import embed_name_change


class logging_nameChanges(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_update(self, before, after):
        if before.nick is None:
            username_before = before
        else:
            username_before = before.nick

        if after.nick is None:
            username_after = after
        else:
            username_after = after.nick

        if before.nick != after.nick and before.nick is not None:
            embed = embed_name_change(before, after, username_before, username_after)

            log_info(f"{username_before} has changed their name to {username_after}.")
            logs_channel = await self.bot.fetch_channel(config['user_log'])
            await logs_channel.send(f'{username_after.mention}', embed=embed)


def setup(bot):
    bot.add_cog(logging_nameChanges(bot))
