"""
This listens for role updates and queries the DB with the new role set
TODO: Move the embeds into the _embed.py file
TODO: Get the config out of here.
"""
import re
from datetime import datetime
import discord
from discord.ext import commands
from __main__ import config
from discord_bot.logs.logger import *


class ModerationInvitations(commands.Cog):
    """
    This cog looks for discord invites and blocks the shit out of them.
    """

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        """
        The cog scans every message sent in the guild
        """
        txt = message.content
        current_channel = message.channel
        logs_channel = await self.bot.fetch_channel(config['mod_log'])

        def is_invite(arg_message):
            """
            Then uses some fancy regex to scan for invites:

            -- Covers official invites "discord.gg/s7s8df9a"
            -- And urls that start with d and end with letter numbers "dxxxx.gg/23bn2u2"
            """

            official = re.search(
                r"(?:https?://)?(?:www\.|ptb\.|canary\.)?(?:"
                r"discord(?:app)?\.(?:(?:com|gg)/invite/["
                r"a-z0-9-_]+)|discord\.gg/[a-z0-9-_]+)",
                arg_message)
            unofficial = re.search(r"(?:https?://)?(?:www\.)?(?:dsc\.gg|"
                                   r"invite\.gg+|discord\.link)/[a"
                                   r"-z0-9-_]+",
                                   arg_message)
            if official is True or unofficial is True:
                return True


        def log_message(arg_message):
            """
            Logs the fact that the scanner found a bad message and removed it.
            """
            author = arg_message.author
            embed = discord.Embed(title='<:red_circle:1043616578744357085> Invite removed'
                                  , description=f'Posted by {arg_message.author}\n'
                                                f'In {arg_message.channel.mention}'
                                  , color=discord.Color.dark_red()
                                  , timestamp=datetime.utcnow())
            embed.set_thumbnail(url=author.avatar)
            embed.add_field(name='Message: '
                            , value=message.content
                            , inline=True)
            log_info(f"{author} sent a discord invite that was caught by spam protection.")
            return embed

        def embed_warning(arg_message):
            """
            Replaces the message with a shameful warning.
            """
            embed = discord.Embed(title='<:x:1055080113336762408> External Invites '
                                        'are not allowed here!',
                                  description=f'{arg_message.author}, your message was removed '
                                              'because it contained an external invite.\nIf this'
                                              ' was a mistake, contact the @staff'
                                  , color=discord.Color.dark_red()
                                  , timestamp=datetime.utcnow())
            return embed

        if is_invite(txt) is True:
            await logs_channel.send(embed=log_message(message))
            await message.delete()
            await current_channel.send(embed=embed_warning(message))


def setup(bot):
    """
    Necessary for loading the cog into the bot instance.
    """
    bot.add_cog(ModerationInvitations(bot))
