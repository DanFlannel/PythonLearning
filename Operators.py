
def add(nums):
    val = nums[0]
    for n in range(1, len(nums)):
        val += nums[n] #this is shorthand for val = val + nums[n] is the same as val += nums[n]
    return val

def sub(nums):
    val = nums[0]
    for n in range(1, len(nums)):
        val -= nums[n]
    return val

def div(nums):
    val = nums[0]
    for n in range(1, len(nums)):
        val /= nums[n]
    return val

def mult(nums):
    val = nums[0]
    for n in range(1, len(nums)):
        val *= nums[n]
    return val