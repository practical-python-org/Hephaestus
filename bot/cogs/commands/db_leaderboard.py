"""
This command grabs the top 10 users with the most points, embeds it, and sends it.
TODO: Pull the config out of here. We should be able to use ctx.guild.id, and
      then move into fetch_member() from there.
"""
from discord.ext import commands
from __main__ import config
from bot.utility._db_functions import see_top_10
from bot.utility._embeds import embed_leaderboard


class DBleaders(commands.Cog):
    """
    Grabs the top 10 using bot/utility/_db_functions/see_top_10
    embed uses bot/utility/_embeds/embed_leaderboard
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='See the top 10 point earners.')
    async def leaderboard(self, ctx):
        """
        grabs the guild, then the member from there.
        then iterates over them and adds each one to its own field.
        """
        data = see_top_10()
        guild = self.bot.get_guild(config['id'])

        embed = embed_leaderboard()
        for person_number, person in enumerate(data):
            member = guild.get_member(person[0])
            embed.add_field(name=f" -- # {person_number+1} --",
                            value=f"{member.display_name} with {person[1]}",
                            inline=False)

        await ctx.respond(embed=embed)


def setup(bot):
    """
    Necessary for loading the cog into the bot instance...
    """
    bot.add_cog(DBleaders(bot))
