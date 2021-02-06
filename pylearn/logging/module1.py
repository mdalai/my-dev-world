
import logging
import commons

# ? why NullHandler
#logger = logging.getLogger(__name__).addHandler(logging.NullHandler)

logger = logging.getLogger(f'{commons.APPNAME}.' + __name__)


def module1_func1():
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')

if __name__ == '__main__':
    print(f'module1: {__name__}')