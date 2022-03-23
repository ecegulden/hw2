#Create function called
def func_counter(func): 
    def wrapper(*args):
        wrapper.counter+= 1
        func(*args)
    wrapper.counter = 0
    return wrapper
