import time


def calculate_time(func):
    def wrapper():
        starting = time.time()
        func()
        ending = time.time()
        print ('Total time',ending - starting)
    return wrapper
