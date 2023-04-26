import os
import sys

import discord  # pip install py-cord
import toml
from discord.ext import commands

from hephaestus.logs.logger import log_debug, log_info

bot = discord.Bot(intents=discord.Intents.all(), owner_id=643393852723691533)

log_info("Loading TOML file...")
config = toml.load("server.toml")
log_info(" - Success.")
log_info(" - Success.")
log_info(" - Success.")


def load_cogs():
    """
    Loads the directories under the /cogs/ folder,
    then digs through those directories and loads the cogs.
    """
    log_info("Loading Cogs...")
    for directory in os.listdir("./cogs"):
        for file in os.listdir(f"./cogs/{directory}"):
            if file.endswith(".py") and not file.startswith("_"):
                log_debug(f"Loading Cog: \\{directory}\\{file}")
                bot.load_extension(f"cogs.{directory}.{file[:-3]}")
    log_info(" - Success.")


def load_key_and_run():
    """
    Loads the bot key as the first arg when running the bot OR from an env variable.
    For example:
        "python main.py BOT_TOKEN_HERE"
    """
    if len(sys.argv) > 1:
        TOKEN = sys.argv[1]
        log_info("Loading Token from arg.")
        bot.run(TOKEN)
    elif os.environ["TOKEN"] is not None:
        log_info("Loading Token from environment variable.")
        bot.run(os.environ["TOKEN"])
    else:
        log_info("ERROR: You must include a bot token.")
        log_info('Example: "python main.py BOT_TOKEN_GOES_HERE"')


if __name__ == "__main__":
    load_cogs()
    load_key_and_run()