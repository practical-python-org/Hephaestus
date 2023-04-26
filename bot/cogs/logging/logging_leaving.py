from discord.ext import commands
from __main__ import config
from logs.logger import log_info
from utility._embeds import embed_leave


class logging_leaving(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Dont log leaves for unapproved people.
        if 'Needs Approval' in [role.name for role in member.roles]:
            return

        current_guild = self.bot.get_guild(config['id'])
        audit_log = [entry async for entry in current_guild.audit_logs(limit=1)][0]

        if str(audit_log.action) != 'AuditLogAction.ban' and str(audit_log.action) != 'AuditLogAction.kick':
            embed = embed_leave(member)

            log_info(f"{member} has left the Guild.")
            logs_channel = await self.bot.fetch_channel(config['join_log'])
            await logs_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(logging_leaving(bot))
