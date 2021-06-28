nums = [1,0,-1,0,-2,2]
#nums=[-5,5,4,-3,0,0,4,-2]


startIndex=0
dummyList=[]
def fourSum(nums,target,index):
    listValue=[]
    for i in range(len(nums)-2):
        for j in range(i+1,len(nums)-1):
                aPointer=j+1
                bPointer=len(nums)-1
                while aPointer<bPointer:
                    print(nums[i],nums[j],nums[aPointer],nums[bPointer])
                    needToSum=[nums[i],nums[j],nums[aPointer],nums[bPointer]]
                    sumValue=sum(needToSum)
                    if sumValue==target:
                        needToSum=list(sorted(needToSum))
                        if needToSum not in listValue:
                            listValue.append(needToSum)
                        aPointer+=1
                        bPointer-=1
                    elif sumValue>target:
                        bPointer-=1
                    else:
                        aPointer+=1
                    
    return listValue
#[[-5,5,4,0],[-5,5,0,4],[5,4,-3,-2],[5,-3,4,-2]]
nums=list(sorted(nums))
#[-2, -1, 0, 0, 1, 2]
#print(nums)
target = 0
print(fourSum(nums,target,startIndex))