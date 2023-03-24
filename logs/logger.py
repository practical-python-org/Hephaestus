import logging

logging.basicConfig(filename="logs/testing.log",
                    format='%(asctime)s - %(levelname)s: %(message)s',
                    datefmt='%Y-%m-%d %H:%M.%S',
                    filemode='w')

logger = logging.getLogger()


def log_debug(thing: object):
    logger.setLevel(logging.DEBUG)
    """
    Takes any printable input.
    Writes it to a log file, as well as prints it in the terminal.
    """
    print(thing)
    logger.info(thing)


def log_info(thing: object):
    logger.setLevel(logging.INFO)

    print(thing)
    logger.info(thing)


def log_warn(thing: object):
    logger.setLevel(logging.WARN)

    print(thing)
    logger.info(thing)


def log_critical(thing: object):
    logger.setLevel(logging.CRITICAL)

    print(thing)
    logger.info(thing)
