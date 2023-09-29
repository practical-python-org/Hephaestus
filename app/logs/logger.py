"""Controls the logging for the entire application.
Also, the logging level is controlled here
TODO: figure out a way to control this externally.
 """
import logging
import pathlib
import json

from colorama import Fore, Style


config = json.load(open('server.json'))

log_file_path = pathlib.Path('logs', config['server_info']['logfile_name'])
logging.basicConfig(filename=log_file_path,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M.%S',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def log_debug(thing: object):
    """ Logs at the debug level """
    logger.debug(thing)


def log_info(thing: object, *success):
    """ Logs at the info level """
    if success:
        print(Fore.GREEN + thing + Style.RESET_ALL)
    else:
        print(thing)
    logger.info(thing)


def log_warn(thing: object):
    """ Logs at the warn level """
    print(Fore.RED + thing + Style.RESET_ALL)
    logger.warning(thing)


def log_critical(thing: object):
    """ Logs at the critical level """
    print(Fore.RED + thing + Style.RESET_ALL)
    logger.critical(thing)
