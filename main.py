import logging

logger = logging.getLogger(__name__)
def add(x, y):
    return x+y

def minus(x, y):
    return x-y

def time(x, y):
    return x*y

def division(x, y):
    return x/y

x = 1
y = 2
print(f'{x} + {y} = {add(x, y)}')
print(f'{x} - {y} = {minus(x, y)}')
print(f'{x} * {y} = {time(x, y)}')
print(f'{x} / {y} = {division(x, y)}')
logging.info(f'{x} + {y} = {add(x, y)}')
logging.info(f'{x} - {y} = {minus(x, y)}')
logging.info(f'{x} * {y} = {time(x, y)}')
logging.info(f'{x} / {y} = {division(x, y)}')