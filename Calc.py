#importing all of our methods in the Operators.py class
import Operators

def calculator(str):

    nums = getNumbers(str)
    operator = getOperator(str)

    if len(nums) is 0:
        print("no numbers found")
        return None

    if operator is None:
        print("no valid operator found")
        return None

    value = getResult(nums, operator)
    print(value)

def getNumbers(str):
    split = str.split()
    list = []
    for s in split:
        if s.isdigit():
            list.append(int(s))
    return list

def getOperator(str):
    split = str.split()
    for s in split:
        if s is '+' or s is '-' or s is '*' or s is '/':
            return s
    return None

def getResult(nums, operator):
    if(operator is None):
        raise Exception("Invalid Operator Exception")

    if(len(nums) is 0):
        raise Exception("Invalid numbers exception")


    if(operator is '+'):
        return Operators.add(nums)
    elif(operator is '-'):
        return Operators.sub(nums)
    elif(operator is '*'):
        return Operators.mult(nums)
    elif(operator is '/'):
        return Operators.div(nums)
    else:
        return None



calculator('2 3 4 5')
calculator("2 + s + 45 - 3") #[2, +, s, +, 45, +, 3]
calculator("5 - 3")
calculator("2 * 5")
calculator("10 / 2")

# arrays SUCK
# lists ARE AWESOME