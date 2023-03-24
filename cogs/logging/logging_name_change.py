import discord
from discord.ext import commands
from datetime import datetime
from __main__ import config
from Hephaestus.logs.logger import log_info


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
            embed = discord.Embed(title=f'<:grey_exclamation:1044305627201142880> Name Change'
                                  , description=f'Changed by: {before}.'
                                  , color=discord.Color.dark_grey()
                                  , timestamp=datetime.utcnow())
            embed.set_thumbnail(url=after.avatar)
            embed.add_field(name='Before', value=username_before, inline=True)
            embed.add_field(name='After', value=username_after, inline=True)

            log_info(f"{username_before} has changed their name to {username_after}.")
            logs_channel = await self.bot.fetch_channel(config['user_log'])  # ADMIN user log
            await logs_channel.send(f'{username_after.mention}', embed=embed)


def setup(bot):
    bot.add_cog(logging_nameChanges(bot))