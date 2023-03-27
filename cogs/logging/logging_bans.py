from discord.ext import commands
from __main__ import config
from Hephaestus.logs.logger import log_info
from Hephaestus.cogs.utility._embeds import embed_ban


class logging_bans(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        # Dont log bans for unapproved people.
        if 'Needs Approval' in [role.name for role in member.roles]:
            return

        # Grab the audit log entry that triggered this cog
        current_guild = self.bot.get_guild(config['id'])
        audit_log = [entry async for entry in current_guild.audit_logs(limit=1)][0]

        if str(audit_log.action) == 'AuditLogAction.ban':
            if audit_log.target == member:

                embed = embed_ban(member, audit_log)

                log_info(f"{member} was banned. Reason:{audit_log.reason}")
                logs_channel = await self.bot.fetch_channel(config['mod_log'])
                await logs_channel.send(embed=embed)
                return


def setup(bot):
    bot.add_cog(logging_bans(bot))
