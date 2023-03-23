import os
import sys
import tomli
import discord
from utility.logger import log

bot = discord.Bot(intents=discord.Intents.all())


def load_toml():
    """
    Loads the TOML file, and uses it across the bot.
    """
    with open("server.toml", "rb") as f:
        f = tomli.load(f)
        log(f"TOML: {f}")
        return f


def load_cogs():
    """
    Loads the directories under the /cogs/ folder,
    then digs through those directories and loads the cogs.
    """
    for directory in os.listdir("./cogs"):
        for file in os.listdir(f"./cogs/{directory}"):
            if file.endswith('.py'):
                log(f"Loading Cog: \\{directory}\\{file}")
                bot.load_extension(f"cogs.{directory}.{file[:-3]}")


def load_key_and_run():
    """
    Loads the bot key as the first arg when running the bot.
    For example:
        "python main.py BOT_TOKEN_HERE"
    """
    if len(sys.argv) > 1:
        TOKEN = sys.argv[1]
        bot.run(TOKEN)
    else:
        log('ERROR: You must include a bot token.')


if __name__ == "__main__":
    config = load_toml()
    load_cogs()
    load_key_and_run()
