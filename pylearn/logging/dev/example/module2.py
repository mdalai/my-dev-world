import logging
import commons

logger = logging.getLogger(f'{commons.APPNAME}.' + __name__)

def main():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == '__main__':
    main()