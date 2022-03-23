import time


#starting the fuction calculate_time

def calculate_time(func):
    def wrapper():
        start= time.time()
        func()
        end = time.time()
        print ("Total Time:", end-start)
    return wrapper
