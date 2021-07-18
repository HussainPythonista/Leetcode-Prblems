nums=[-2,-2,-4,-1,2,1,3,1-4,5]
aPointer=0
while nums[aPointer]<0:
    aPointer+=1
bPointer=len(nums)-1
while nums[bPointer]>0:
    bPointer-=1
nums[aPointer],nums[bPointer]=nums[bPointer],nums[aPointer]

print(nums)