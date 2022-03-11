#Create function called
def func_counter(n):  
    def wrapper(y):
        #variable to track the number of times the function being decorated is called.
        wrapper.counter += 1
        return n
    wrapper.counter = 0
    return wrapper

@func_counter  
def foo(y):
    return y+2**3-34
    
y=int(input("Enter a number:")) 
foo(y)
foo(y) 

print(foo.counter) 
