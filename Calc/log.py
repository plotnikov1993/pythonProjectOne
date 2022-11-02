from datetime import datetime as dt
from time import time

def log(data):
    with open('log1.csv', 'a') as file:
        file.write(f'\n{data}')