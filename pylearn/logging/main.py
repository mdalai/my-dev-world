
import argparse

from module1 import module1_func1
from dev.example import module2
import commons

import logging
from mylog.mylogging import config_console_logger, config_file_logger

logger = logging.getLogger(commons.APPNAME)
logger = config_file_logger(logger, log_file=commons.LOG_FILEPATH)


def main():
    global logger
    parser = argparse.ArgumentParser()
    parser.add_argument('--debug','-d', action='store_true', help='debug mode')
    args = parser.parse_args()
    if args.debug:
        logger = config_console_logger(logger)

    log_msgs()
    module1_func1()
    module2.main()

def log_msgs():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')


if __name__ == '__main__':
    main()
    