"""
__main__.py entrypoint for the bot.
Loads a TOML, Loads the cogs, grabs token from args or env vars
Runs the bot
"""
import discord  # pip install py-cord
from logs.logger import *
from utility._cog_loader import load_cogs
from utility._token_loader import load_key_and_run


bot = discord.Bot(intents=discord.Intents.all())

log_info("Loading config file...")
config = json.load(open('server.json'))
log_info(" - Success.")


if __name__ == "__main__":
    load_cogs(bot)
    load_key_and_run(bot)
