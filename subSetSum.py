nums = [2, 7, 3, 5, 4]
sumValue = 0
target = 15
path = [0 for i in range(len(nums))]
newVal = []


def sumOfSubSet(nums, target, n, path):
    global sumValue, newVal
    if sumValue == target:
        return path
    elif sumValue > target:
        return
    elif n <= len(nums)-1:
        newVal.append(path)
        sumValue += nums[n]
        path[n] = 1
        sumOfSubSet(nums, target, n+1, path)
        path[n] = 0
        sumValue -= nums[n]
        sumOfSubSet(nums, target, n+1, path)
        


val = sumOfSubSet(nums, target, 0, path)
print(val)
