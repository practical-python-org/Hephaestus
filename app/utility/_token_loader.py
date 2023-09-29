import os
import sys
from logs.logger import *


def load_key_and_run(discord_client):
    """
    Loads the bot key as the first arg when running the bot OR from an env variable.
    For example:
        "python __main__.py BOT_TOKEN_HERE"
    """
    try:
        if len(sys.argv) > 1:  # Check args for the token first
            token = sys.argv[1].replace('TOKEN=','')

            log_info('Loading Token from arg.')
            discord_client.run(token)

        elif os.environ['TOKEN'] is not None:  # if not in args, check the env vars
            log_info('Loading Token from environment variable.')
            discord_client.run(os.environ['TOKEN'])


        else:
            log_warn('\nERROR: You must include a bot token.')
            log_warn('Example: "python __main__.py BOT_TOKEN_GOES_HERE"')
    except KeyError as noToken:
        log_warn('\nERROR: You must include a TOKEN variable, either in an ARG or in an ENV var. ')
        log_warn('Example: "python __main__.py BOT_TOKEN_GOES_HERE"')