import logging
import sys


'''
stdout
file
'''


LOG_FILE_NAME = 'person.log'


def get_logger():
    logger = logging.getLogger(__name__)
    formatter = logging.Formatter('%(asctime)s  - %(levelname)s  - %(funcName)s - %(message)s')

    screen_handler = logging.StreamHandler(sys.stdout)
    screen_handler.setLevel(logging.DEBUG)
    screen_handler.setFormatter(formatter)

    logfile_handler = logging.FileHandler(filename=LOG_FILE_NAME)
    logfile_handler.setLevel(logging.DEBUG)
    logfile_handler.setFormatter(formatter)


    logger.addHandler(logfile_handler)
    logger.addHandler(screen_handler)
    logger.setLevel(logging.DEBUG)


    return logger