nums = [-2,1]
#nums=[-2,1,-3,4,-1,2,1,-5,4]
#nums = [5,4,-1,7,8]
def maximumOfSubArray(nums):
    currentMaximum=nums[0]
    maximumOfMaximum=0
    for i in range(1,len(nums)):
        currentMaximum=max(nums[i],currentMaximum+nums[i])
        maximumOfMaximum=max(maximumOfMaximum,currentMaximum)
    print(maximumOfMaximum)

def forCrossMaximum(nums,mid):
    leftmaxOfMax=-177838383494847839822
    leftmax=0
    for toFindMaxInLeft in range(mid-1,-1,-1):
        leftmax+=nums[toFindMaxInLeft]
        leftmaxOfMax=max(leftmaxOfMax,leftmax)
    rightMax=0
    rightmaxOfMax=-177838383494847839822
    for toFindMaxInRight in range(mid,len(nums)):

        rightMax+=nums[toFindMaxInRight]
        rightmaxOfMax=max(rightmaxOfMax,rightMax)

    return max(leftmaxOfMax,rightmaxOfMax,leftmaxOfMax+rightmaxOfMax)
def maxSubArray(nums):
    if len(nums)==1:
        
        return nums[0]
    else:
        #Spliting the array
        mid=len(nums)//2
        left=maxSubArray(nums[:mid])
        right=maxSubArray(nums[mid:])
        return max(left,right,forCrossMaximum(nums,mid))
print(maxSubArray(nums))