
def doubler(func):
    def wrapper():
        return wrapper
        
@doubler  
def foofoo(n):
    return n*2

n=int(input("Enter:"))
    
print(doubler(foofoo))

