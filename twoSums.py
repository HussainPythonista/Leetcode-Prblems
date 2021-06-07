from sys import api_version


#nums = [-10,7,19,15]
nums=[2,7,11,15]

target =9
def twoSum(nums,target):
    dictValue={}
    for i in range(len(nums)):
        complement=target-nums[i]
        
        if complement in dictValue:
            return dictValue[complement],i
        else:
            dictValue[nums[i]]=i
            
print(twoSum(nums,target))