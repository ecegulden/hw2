
#doubler definition
def doubler(func):
    def wrapper():
        x= func()*2
        return x
        
    return wrapper
@doubler
def numres():
    return 10
print(numres())
