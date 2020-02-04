def stringManipulator(a):
    new_string = ""
    counter = 0
    for x in a:
        if counter % 2 == 0:
            new_string += x.upper()
        else:
            new_string += x.lower()
        counter += 1
    print(new_string)
    return new_string



def indexedForLoop(a):
    new_string = ""
    for index in range(len(a)):
        new_string += getCharacterValue(a[index], index)
    print(new_string)
    return new_string


def getCharacterValue(c, index):
        if index % 2 == 0:
            return c.upper()
        else:
            return c.lower()



def evenLessCode(a):
    new_string = ""
    for index in range(len(a)):
        if index % 2 == 0: new_string += a[index].upper()
        else: new_string += a[index].lower()
    print(new_string)
    return new_string


def epsilonIsntSupportedInPythonAndThatSucks(a):
    new_string = ""
    for index in range(len(a)):
        #this isn't legal in python and that sucks but it would be so clean
        #new_string += (index % 2 == 0) ? a[index].upper : a[index].lower()
        pass
    print(new_string)
    return new_string



stringManipulator("hello")
indexedForLoop("hello")
evenLessCode("hello")