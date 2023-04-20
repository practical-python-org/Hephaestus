import logging
import pathlib


log_file_path = pathlib.Path('bot', 'logs', "Hephaestus_logs.log")
logging.basicConfig(filename=log_file_path,
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M.%S',
                    filemode='w')

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)


"""
Takes any printable input.
Writes it to a log file, as well as prints it in the terminal.
"""


def log_debug(thing: object):
    # print(thing)
    logger.debug(thing)


def log_info(thing: object):
    print(thing)
    logger.info(thing)


def log_warn(thing: object):
    print(thing)
    logger.warning(thing)


def log_critical(thing: object):
    print(thing)
    logger.critical(thing)
