#starting the sort fuction
def sort_list(myList):
    # define n to be the length of the input list
    n=len(myList)
    
    i=0
    # A nested while loop where the first loop will
    #iterate over the whole list
    # index of the first loop be i
    while(i<n):
        j=0
        #second loop should only loop over the list first n-i-1 elements
        while(j<n-i-1):
            # if the value at the current location is larger than the next value
            #then swap them
            if(myList[j]>myList[j+1]):
                new=myList[j]
                myList[j]=myList[j+1]
                myList[j+1]=new
            j=j+1
        i=i+1
     
    #  return a list   
    return myList

# getting one of the examples that was given in the instructions    
myList=[1,3,2,7]
# Calling the function
ans=sort_list(myList)

# sorted list
for i in ans:
    print(i,end=" ")


