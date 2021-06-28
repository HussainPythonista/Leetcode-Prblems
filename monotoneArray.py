def monoToneArray(nums):
    aPointer=0
    bPointer=len(nums)-1
    dp=[False for _ in range(len(nums)-1)]
    if nums[aPointer]<nums[bPointer]:
        for i in range(1,len(nums)):
            if nums[i-1]>nums[i]:   
                return False
            
        return True
               
    else:
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                return False
            
        return True
    
            
nums=[1,3,2]
print(monoToneArray(nums))