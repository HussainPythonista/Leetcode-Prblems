nums = [3,3]
target = 6
def twoSum(nums,target):
    dictValue={}
    for i in range(len(nums)):
        complement=target-nums[i]
        if complement not in dictValue:
            dictValue[nums[i]]=i
        else:
            print(dictValue[complement],i)
        print(dictValue)
twoSum(nums,target)
