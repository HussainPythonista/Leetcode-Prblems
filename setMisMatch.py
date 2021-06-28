def setMisMatch(nums):
    setValue=[]
    sumValue=0
    result=[]
    for i in range(len(nums)):
        if nums[i] not in setValue:
            setValue.append(nums[i])
            sumValue+=nums[i]
        else:
            result.append(nums[i])
    n=len(nums)
    sumOfNaturalNumber=n*(n+1)/2
    result.append(int(sumOfNaturalNumber-sumValue))

    return result
nums = [1,2,2,4]
print(setMisMatch(nums))