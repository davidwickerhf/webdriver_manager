import logging
import os

LOGGER:logging.Logger = None


def log(text, logger:logging.Logger=None, filename:str=None, level=logging.INFO, formatter='[%(name)s] - %(message)s'):
    if logger:
        logger.info(f'WDM: {text}')
        LOGGER = logger
        return
    
    formatter = logging.Formatter(formatter)
    if filename:
        handler = logging.FileHandler(filename)
    else:
        handler = logging.StreamHandler()
    
    if not LOGGER:
        LOGGER = logging.getLogger('WDM')
    
    handler.setFormatter(formatter)
    LOGGER.addHandler(handler)
    LOGGER.setLevel(level)
    LOGGER.info(text)