from discord.ext import commands
from __main__ import config
from utility._DB_Functions import see_top_10
from utility._embeds import embed_leaderboard


class db_commands(commands.Cog, command_attrs=dict(hidden=True)):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='See the top 10 point earners.')
    async def leaderboard(self, ctx):
        data = see_top_10()
        guild = self.bot.get_guild(config['id'])

        embed = embed_leaderboard()
        for person_number, person in enumerate(data):
            member = guild.get_member(person[0])
            embed.add_field(name=f" -- # {person_number} --",
                            value=f"{member.display_name} with {person[1]}",
                            inline=False)

        await ctx.respond(embed=embed)


def setup(bot):
    bot.add_cog(db_commands(bot))
