import logging


logging.basicConfig(filename="utility/testing.log",
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M.%S',
                    filemode='w')

logger = logging.getLogger()

logger.setLevel(logging.INFO)


def log(thing: object):
    """
    Takes any printable input.
    Writes it to a log file, as well as prints it in the terminal.
    """
    print(thing)
    logger.info(thing)
