"""
main.py entrypoint for the bot.
Loads a TOML, Loads the cogs, grabs token from args or env vars
Runs the bot
"""
import os
import sys
import toml
import discord  # pip install py-cord
from logs.logger import log_info, log_debug

bot = discord.Bot(intents=discord.Intents.all())

log_info("Loading TOML file...")
config = toml.load('server.toml')
log_info(" - Success.")
log_info("LINT ME BITCH")

def load_cogs():
    """
    Loads the directories under the /cogs/ folder,
    then digs through those directories and loads the cogs.
    """
    log_info("Loading Cogs...")
    for directory in os.listdir("./cogs"):
        if not directory.startswith("_"):  # Makes sure __innit.py__ doesnt get called
            for file in os.listdir(f"./cogs/{directory}"):
                if file.endswith('.py') and not file.startswith("_"):
                    log_debug(f"Loading Cog: \\{directory}\\{file}")
                    bot.load_extension(f"cogs.{directory}.{file[:-3]}")
    log_info(" - Success.")


def load_key_and_run():
    """
    Loads the bot key as the first arg when running the bot OR from an env variable.
    For example:
        "python main.py BOT_TOKEN_HERE"
    """
    if len(sys.argv) > 1:  # Check args for the token first
        TOKEN = sys.argv[1]
        log_info('Loading Token from arg.')
        bot.run(TOKEN)

    elif os.environ['TOKEN'] is not None:  # if not in args, check the env vars
        log_info('Loading Token from environment variable.')
        bot.run(os.environ['TOKEN'])


    else:
        log_info('ERROR: You must include a bot token.')
        log_info('Example: "python main.py BOT_TOKEN_GOES_HERE"')


if __name__ == "__main__":
    load_cogs()
    load_key_and_run()
