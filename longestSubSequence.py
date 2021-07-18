nums = [10, 9, 2, 5, 3, 7, 101, 18]
#nums = [0, 1, 0, 3, 2, 3]


nums = [4, 10, 4, 3, 8, 9]


#nums=[4,5,8]
#
#Efficient dynamic Approach
def findingLongestSubSequence(listValue):
    memoization = [1 for i in range(len(listValue))]
   # for _ in range(len(listValue))]#We Set 1 Because Every single element is increasing by Itself
                   
    maxValue = 0
    for i in range(len(listValue)):
        for j in range(i):
            #print(listValue[i],listValue[j])
            if listValue[i] > listValue[j] and memoization[i]<=memoization[j]:
                    #print(memoization[i])
                    memoization[i] = memoization[j]+1
            # print(memoizationn)
            # maxValue=max(maxValue,memoization[i])
    return memoization
    
     
print(findingLongestSubSequence(nums))
#Im trying to solve same Subsequence by Backtrackin algorithm

#
memoization=[-1 for _ in range(len(nums))]

#Brute Force Recursion
def helperFunction(nums,i):
    global memoization
    if i==0:
        return 1
    ans=1
    for n in range(i-1,-1,-1):
        if nums[i]>nums[n]:
            ans=max(ans,1+helperFunction(nums,n))
    return ans

def longestSubSequence(nums):
    maxValue=0
    for i in range(len(nums)):
        maxValue=max(maxValue, helperFunction(nums,i))

    print(maxValue)

def backTrackingApproach(nums):
    pass
def twoSum(nums,target):
    forFastAccess={}
    for i in range(len(nums)):
        if nums[i] not in forFastAccess:
            forFastAccess[target-nums[i]]=i
        else:
            print(forFastAccess[nums[i]],i)

    print(forFastAccess)
nums = [3,2,4]
target = 6
#twoSum(nums,target)

def lis(a):
    n=len(a)
    # Creating the sorted list
    b=sorted(list(set(a)))
    m=len(b)
     
     
    # Creating dp table for storing the answers of sub problems
    dp=[[-1 for i in range(m+1)] for j in range(n+1)]
     
    # Finding Longest common Subsequence of the two arrays
    for i in range(n+1):
             
        for j in range(m+1):
            if i==0 or j==0:
                dp[i][j]=0
            elif a[i-1]==b[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp
a=nums = nums = [0, 1, 0, 3, 2, 3]


print(lis(a))