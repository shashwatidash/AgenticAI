from logger import logging

def add(a, b):
    logging.debug("Addition operation is taking place")
    return a + b

add(2, 5)