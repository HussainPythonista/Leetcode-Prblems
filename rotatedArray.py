def findingPiviot(nums):
    if nums[0] > nums[len(nums)-1]:
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                return i
    else:
        return len(nums)-1


def findValueInRotatedArray(nums, valToFind):
    piviot = findingPiviot(nums)
    left = 0
    right = len(nums)-1
    if valToFind <= nums[piviot] and nums[left] <= valToFind:
        right = piviot
    else:
        left = piviot+1

    while left <= right:
        mid = (left+right)//2
        if nums[mid] < valToFind:
            left = mid+1
        elif nums[mid] > valToFind:
            right = mid-1
        else:

            return mid
    else:
        return -1


nums = [1, 3]

valToFind = 0
print(findValueInRotatedArray(nums, valToFind))

# Another Method


def valueInRotatedArray(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        else:
            if nums[left] <= nums[mid]:
                if target >= nums[left] and target < nums[mid]:
                    right = mid-1
                

            else:
                if target <= nums[right] and target < nums[mid]:
                    left = mid+1
                


target = 0
nums = [4, 5, 6, 7, 0, 1, 2]
print(valueInRotatedArray(nums, target))

""""start=0
        end=len(nums)-1
        while start<=end:
            mid=(start+end)//2
            if nums[mid]==target:
                return mid
            else:
                if nums[start]<=nums[mid]:
                    if nums[start]<=target and nums[mid]>target:
                        end=mid-1
                    else:
                        start=mid+1
                else:
                    if nums[mid]<target and target<=nums[end]:
                        start=mid+1
                    else:
                        end=mid-1
        else:
            return -1 """
