from collections import namedtuple

def sumation1(a):
    if len(a) == 0: 
        return 0
    total = 0
    canAdd = True
    for x in a:
        if x == 6:
            canAdd = False
        elif x == 9 and canAdd == False:
            canAdd = True
        else:
            if canAdd:
                total = total + x
    return total

#excludes the 6 and the 9 from our calculations
def summation2Exclusive(arr):
    if(len(arr) == 0): return 0
    total = 0
    canAdd = True
    for x in arr:
        tmp = canAdd #make sure we do not include the 9 as we switch back to being able to add
        canAdd = getCanAdd(canAdd, x)
        if(tmp and canAdd) : total = total + x
    return total

#includes the 6 and the 9 in our calculations
def summation2Inclusive(arr):
    if(len(arr) == 0): return 0
    total = 0
    canAdd = True
    for x in arr:
        tmp = canAdd
        canAdd = getCanAdd(canAdd, x)
        if(canAdd or canAdd != tmp) : total = total + x
    return total

def summation3(arr):
    if(len(arr) == 0): return 0
    total = 0
    canAdd = True
    for x in arr:
        nTuple = getNamedTuple(canAdd, x)
        canAdd = nTuple.canAdd
        total = total + nTuple.value
    return total


def getCanAdd(b, x):
    if(x == 6): 
        return False
    elif(x == 9 and b == False):
        return True
    else:
        return b

def getNamedTuple(b, x):
    Point = namedtuple('Point', 'canAdd value')
    if(x == 6):
        return Point(False, 0)  # change the value to 6 to make the 6 inclusive
    elif(x == 9 and b == False):
        return Point(True, 0)   # change the value to 9 to make the 9 inclusive
    elif(b == False):
        return Point(False, 0)
    else:
        return Point(True, x)

array = [1,6,7,8,9,1,2,3]
print(sumation1(array))
print(summation2Exclusive(array))
print(summation2Inclusive(array))
print(summation3(array))
