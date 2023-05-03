"""
Logs messages that get deleted.
TODO: Pull config out of here.
"""
from discord.ext import commands
from __main__ import config
from discord_bot.logs.logger import *
from discord_bot.utility._embeds import embed_message_delete


class LoggingMessageDelete(commands.Cog):
    """
    Simple listener to on_message_delete
    then checks the audit log for exact details
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        """
        then we grab the guild, and from there read the last entry in the audit log.
        """
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
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(LoggingMessageDelete(bot))
