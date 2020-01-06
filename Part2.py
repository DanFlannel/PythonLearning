x = 1 #this is a global variable that can be used anywhere

def variables1():
    print(x)
    
    y = 2 # this is a local variable
    print(x + y)

def variables2():
    print(x + y) # this will fail because it is trying to add a local and global variable but the local variable doesn't exist in this method

variables1() #this works because y is local to the method variables1, this is a local variable
#variables2() #this fails because y is not defined in variables2 hence it is not global

"""
there are two types of loops
iterative aka for loops or while loops
recursive done worry about it
"""

#recursion can be used like this a method calls itself
def recursive(var):
    if var is 1:
        return None
    else:
        var -= 1
    print(var)
    recursive(var)

recursive(10)