import logging

logging.basicConfig(
    level = logging.DEBUG,
    format = '%(asctime)s-%(name)s-%(levelname)s-%(message)s',
    datefmt = '%Y-%m-%d %H:%M:%S',
    handlers = [
        logging.FileHandler('applog.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('ArithmeticApp')

def add(a, b):
    res = a + b
    logger.debug(f'Adding {a} + {b} = {res}')
    return res

def division(a, b):
    try:
        res = a / b
        logger.debug(f'Adding {a} / {b} = {res}')
        return res
    except ZeroDivisionError:
        logger.error('Divide by zero error')
        return None

add(15, 10)
division(15, 100)
division(15, 0)