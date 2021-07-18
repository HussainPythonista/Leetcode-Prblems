nums=[3,4,5,6,2,1,3,5,6]
def rotation(nums):
    first=nums[0]
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[-1]=first
    return (nums)
print(rotation(nums))


#Shifting all element in left
def leftShift(nums):
    
    for i in range(1,len(nums)):
        nums[i-1]=nums[i]
    nums[-1]=0
    return (nums)
print(leftShift(nums))