import discord
from datetime import datetime
from __main__ import config


def embed_avatar(before, after):
    embed = discord.Embed(
        title=f'{before} updated their profile picture!'
        , color=discord.Color.dark_grey()
        , timestamp=datetime.utcnow()
    )

    embed.set_thumbnail(
        url=after.avatar
    )

    return embed


def embed_ban(some_member, audit_log_entry):
    embed = discord.Embed(
        title=f'<:red_circle:1043616578744357085> {some_member} was banned'
        , description=f'By: {audit_log_entry.user}'
        , color=discord.Color.red()
        , timestamp=datetime.utcnow()
    )

    embed.add_field(
        name=f'Reason:'
        , value=f'{audit_log_entry.reason}'
        , inline=True
    )

    return embed


def embed_kick(some_member, audit_log_entry):
    embed = discord.Embed(
        title=f'<:red_circle:1043616578744357085> {some_member} was kicked'
        , description=f'By: {audit_log_entry.user}'
        , color=discord.Color.red()
        , timestamp=datetime.utcnow()
    )

    embed.add_field(
        name=f'Reason:'
        , value=f'{audit_log_entry.reason}'
        , inline=True
    )
    return embed


def embed_leave(some_member):
    embed = discord.Embed(
        title='\u200b'
        , description=f'{some_member} has left us.'
        , color=discord.Color.red()
        , timestamp=datetime.utcnow()
    )

    return embed


def embed_message_delete(some_member, some_message):
    embed = discord.Embed(
        title=f'<:red_circle:1043616578744357085> Deleted Message'
        , description=f'{some_member.display_name} deleted a message \nIn {some_message.channel.mention}\nMessage '
                      f'author: {some_message.author}'
        , color=discord.Color.dark_red()
        , timestamp=datetime.utcnow()
    )

    embed.set_thumbnail(
        url=some_member.avatar
    )
    if len(some_message.content) > 1020:
        the_message =  some_message.content[0:1020] + '...'
    else:
        the_message = some_message.content
    embed.add_field(
        name='Message: '
        , value=the_message
        , inline=True
    )

    return embed


def embed_message_edit(some_username, orig_author, some_message_before, some_message_after):
    embed = discord.Embed(
        title=f'<:orange_circle:1043616962112139264> Message Edit'
        , description=f'Edited by {some_username}\nIn {some_message_after.channel.mention}'
        , color=discord.Color.dark_orange()
        , timestamp=datetime.utcnow()
    )

    embed.set_thumbnail(
        url=orig_author.avatar
    )

    embed.add_field(
        name='Original message: '
        , value=some_message_before.content
        , inline=True
    )

    embed.add_field(
        name="After editing: "
        , value=some_message_after.content
        , inline=True
    )

    return embed


def embed_name_change(name_before, name_after, username_before, username_after):
    embed = discord.Embed(
        title=f'<:grey_exclamation:1044305627201142880> Name Change'
        , description=f'Changed by: {name_before}.'
        , color=discord.Color.dark_grey()
        , timestamp=datetime.utcnow()
    )

    embed.set_thumbnail(
        url=name_after.avatar
    )

    embed.add_field(
        name='Before'
        , value=username_before
        , inline=True
    )

    embed.add_field(
        name='After'
        , value=username_after
        , inline=True
    )

    return embed


def embed_unban(some_member):
    embed = discord.Embed(
        title=f'<:green_circle:1046088647759372388> User Un-Banned'
        , color=discord.Color.red()
        , timestamp=datetime.utcnow()
    )

    embed.add_field(
        name=f'{some_member.name} was un-banned.'
        , value='Welcome back.'
        , inline=True
    )

    return embed


def embed_leaderboard():
    embed = discord.Embed(
        title=f"{config['name']}'s Top Point earners"
        , color=discord.Color.gold()
        , timestamp=datetime.utcnow()
    )

    embed.set_thumbnail(
        url=config['logo']
    )

    return embed

def embed_user_profile(some_member_info):
    member = some_member_info[0]
    name = member[1] + str(member[2])
    roles = member[5]
    roles = roles.replace('[', '').replace(']', '').replace("'", "").split(',')
    rolestr = ''
    for i in roles:
        rolestr = rolestr + i + '\n'
    image = member[7]
    joined_at = member[8]
    points = member[9]

    embed = discord.Embed(
        title = f"{name}'s Profile"
        , color = discord.Color.green()
        , timestamp=datetime.utcnow()
    )
    embed.add_field(
        name=f"Roles: "
        , value=rolestr
        , inline=False
    )
    embed.add_field(
        name=f"Joined at: "
        , value=joined_at
        , inline=False
    )
    embed.add_field(
        name=f"Points: "
        , value=points
        , inline=False
    )

    embed.set_thumbnail(
        url=image
    )
    return embed


