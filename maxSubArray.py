def maxSubArray(nums):#use Kadanes's Algorithm for this maxSubArray
    if len(nums)>1: 
        maxValue=nums[0]
        maximumAtFinal=nums[0]
        for i in range(len(nums)):
            maxValue=max(nums[i],nums[i]+maxValue)
            maximumAtFinal=max(maximumAtFinal,maxValue)
            print(maximumAtFinal)
        print(maximumAtFinal)
        
        
