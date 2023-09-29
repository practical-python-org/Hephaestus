import os
from logs.logger import *


def load_cogs(discord_client):
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
                    discord_client.load_extension(f"cogs.{directory}.{file[:-3]}")
    log_info(" - Success.", True)