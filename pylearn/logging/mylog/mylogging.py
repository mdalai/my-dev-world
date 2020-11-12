
import logging
import logging.handlers as handlers

LOG_MAX_BYTES=1000000
LOG_BACKUP_COUNT=3

ROOT_LOGGER = logging.getLogger()
ROOT_LOGGER.setLevel(logging.DEBUG)


def _get_loglevel(loglevel):
    num_loglevel = getattr(logging, loglevel.upper(), None)
    if not isinstance(num_loglevel, int):
        raise ValueError(f'Invalid log level: {loglevel}')
    return num_loglevel


def file_logger(log_file, loglevel='WARNING'):
    if not log_file:
        raise ValueError(f'Invalid log file: {log_file}')
    log_level = _get_loglevel(loglevel) 
    fileHandler = logging.FileHandler(log_file)
    fileHandler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    ROOT_LOGGER.addHandler(fileHandler)
    return ROOT_LOGGER

def console_logger(loggername='consoleLogger',loglevel='DEBUG'):
    log_level = _get_loglevel(loglevel)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    ROOT_LOGGER.addHandler(ch)
    return ROOT_LOGGER


def file_logger2(log_file, loglevel='ERROR'):
    if not log_file:
        raise ValueError(f'Invalid log file: {log_file}')
    log_level = _get_loglevel(loglevel)  
    fileHandler = handlers.RotatingFileHandler(log_file,maxBytes=LOG_MAX_BYTES, backupCount=LOG_BACKUP_COUNT)
    fileHandler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    ROOT_LOGGER.addHandler(fileHandler)
    return ROOT_LOGGER

def config_console_logger(logger, loglevel='DEBUG'):
    log_level = _get_loglevel(loglevel)
    ch = logging.StreamHandler()
    ch.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    try:
        logger.addHandler(ch)
    except Exception as e:
        print(f'Unexpected logger error: {e}')
        raise 
    return logger

def config_file_logger(logger, 
                    log_file, 
                    log_maxbytes=1000000, 
                    log_backupcount=3,
                    loglevel='ERROR'):
    if not logger:
        raise ValueError(f'Invalid logger: {logger}')
    if not log_file:
        raise ValueError(f'Invalid log file: {log_file}')
    log_level = _get_loglevel(loglevel)  
    fileHandler = handlers.RotatingFileHandler(log_file, maxBytes=log_maxbytes, backupCount=log_backupcount)
    fileHandler.setLevel(log_level)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    fileHandler.setFormatter(formatter)
    try:
        logger.addHandler(fileHandler)
    except Exception as e:
        print(f'Unexpected logger error: {e}')
        print()
        raise 
    return logger

