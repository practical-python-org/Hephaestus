import discord
from discord.ext import commands
from datetime import datetime
from __main__ import config
from Hephaestus.logs.logger import log_info


class logging_bans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        current_guild = self.bot.get_guild(config['id'])

        # Dont log kicks for unapproved people.
        if 'Needs Approval' in [role.name for role in member.roles]:
            return

        audit_log = [entry async for entry in current_guild.audit_logs(limit=1)][0]

        if str(audit_log.action) == 'AuditLogAction.ban':
            if audit_log.target == member:
                logs_channel = await self.bot.fetch_channel(config['mod_log'])
                embed = discord.Embed(title=f'<:red_circle:1043616578744357085> {member} was banned'
                                      , description=f'By: {audit_log.user}'
                                      , color=discord.Color.red()
                                      , timestamp=datetime.utcnow())
                embed.add_field(name=f'Reason:'
                                , value=f'{audit_log.reason}'
                                , inline=True)

                log_info(f"{member} was banned. Reason:{audit_log.reason}")
                await logs_channel.send(embed=embed)
                return


def setup(bot):
    bot.add_cog(logging_bans(bot))
