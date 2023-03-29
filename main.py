import os
import sys
import tomli
import discord  # pip install py-cord
from Hephaestus.cogs.utility._DB_create import create_db
from logs.logger import log_info, log_debug

bot = discord.Bot(intents=discord.Intents.all())
with open("server.toml", "rb") as f:
    config = tomli.load(f)
    log_info("Loading TOML file...")


def load_cogs():
    """
    Loads the directories under the /cogs/ folder,
    then digs through those directories and loads the cogs.
    """
    log_info("Loading Cogs...")
    for directory in os.listdir("./cogs"):
        for file in os.listdir(f"./cogs/{directory}"):
            if file.endswith('.py') and not file.startswith("_"):
                log_debug(f"Loading Cog: \\{directory}\\{file}")
                bot.load_extension(f"cogs.{directory}.{file[:-3]}")


def load_key_and_run():
    """
    Loads the bot key as the first arg when running the bot.
    For example:
        "python main.py BOT_TOKEN_HERE"
    """
    if len(sys.argv) > 1:
        TOKEN = sys.argv[1]
        log_info(f"Bringing bot online... ")
        bot.run(TOKEN)
    else:
        log_info('ERROR: You must include a bot token.')


if __name__ == "__main__":
    load_cogs()
    load_key_and_run()
    create_db(bot, config['Database_name'], config['id'])

