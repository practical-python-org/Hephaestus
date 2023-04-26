from discord.ext import commands
from __main__ import config
from logs.logger import log_debug, log_info
from utility._embeds import embed_message_delete


class logging_message_delete(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        current_guild = self.bot.get_guild(config['id'])
        audit_log = [entry async for entry in current_guild.audit_logs(limit=1)][0]
        log_debug(audit_log)

        if str(audit_log.action) == 'AuditLogAction.message_delete':
            member = current_guild.get_member(audit_log.user.id)

            embed = embed_message_delete(member, audit_log.target, message)

            log_info(f"{member} deleted a message.")
            logs_channel = await self.bot.fetch_channel(config['mod_log'])
            await logs_channel.send(embed=embed)


def setup(bot):
    bot.add_cog(logging_message_delete(bot))
