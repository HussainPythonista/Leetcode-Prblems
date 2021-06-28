def arithmaticSlices(nums):
    memo=[0 for i in range(len(nums))]
    sumValue=0
    for i in range(len(nums)-2):
        if nums[i+2]-nums[i+1]==nums[i+1]-nums[i]:
            sumValue+=1
            if memo[i+2]==0 and memo[i+1]==0:
                memo[i+2]=1
            else:
                memo[i+2]+=memo[i+1]+ 1
    print(sum(memo))
    

nums = [1, 2, 3]
arithmaticSlices(nums)
