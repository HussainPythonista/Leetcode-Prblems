

def isArrayIsSortedOrNor(nums):
    memoization = [False for i in range(len(nums))]
    memoization[0] = True
    for i in range(1, len(nums)):
        if nums[i] <= nums[i-1]:
            return False

    return True


nums = [2, 3, 6, 7, 9]
print(isArrayIsSortedOrNor(nums))


def reverseTheArray(nums):
    aPointer = 0
    bPointer = len(nums)-1
    while aPointer < bPointer:
        nums[aPointer], nums[bPointer] = nums[bPointer], nums[aPointer]
        aPointer += 1
        bPointer -= 1
    return nums


def InserElementInSortedArray(nums, element):
    nums.append(0)
    bPointer = len(nums)-2
    while nums[bPointer] > element and bPointer >= 0:
        nums[bPointer+1] = nums[bPointer]
        nums[bPointer] = element
        bPointer -= 1
        
    print(nums)


element = 8

InserElementInSortedArray(nums, element)
