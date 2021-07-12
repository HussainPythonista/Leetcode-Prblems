nums = [-2,1,-3,4,-1,2,1,-5,4]
def maximumOfSubArray(nums):
    currentMaximum=nums[0]
    maximumOfMaximum=0
    for i in range(1,len(nums)):
        currentMaximum=max(nums[i],currentMaximum+nums[i])
        maximumOfMaximum=max(maximumOfMaximum,currentMaximum)
    print(maximumOfMaximum)

maximumOfSubArray(nums)
def maxSubArray(nums):
    #Spliting the array
        print(nums)
        left=0
        right=len(nums)-1
        mid=(left+right)//2
        maxSubArray(nums[:mid])
        maxSubArray(nums[mid:])
        

maxSubArray(nums)