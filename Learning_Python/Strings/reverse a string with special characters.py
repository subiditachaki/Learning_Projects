# reverse a string without reversing special characters

def reversedstring(string):
    
    # initialize empty string
    lst = []

    # convert input string to list
    for i in range(0,len(string)):
        lst.append(string[i])
        
    i=0
    j=len(string)-1
    
    # Reverse the list
    while i < j:
        if not lst[i].isalpha():
            i+=1 
        elif not lst[j].isalpha():
            j-=1 
        else:
            lst[i], lst[j] = lst[j],lst[i]
            i+=1 
            j-=1 
    
    # convert the list to string and return
    return ''.join(lst)

# Driver program to test the above function   
string = "a,b$c"
result = reversedstring(string)
print result