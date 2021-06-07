#Three Sum
def threeSum(listValue):
    valueAfterSort=sorted(listValue)#Sort the Values for clear Understanding
    result=[]
    
    for i in range(len(listValue)):
        aPointer=i+1
        bPointer=len(valueAfterSort)-1
        while aPointer<bPointer:
            if valueAfterSort[aPointer]+valueAfterSort[bPointer]<-valueAfterSort[i]:
                aPointer+=1
            elif valueAfterSort[aPointer]+valueAfterSort[bPointer]>-valueAfterSort[i]:
                bPointer-=1
            elif valueAfterSort[aPointer]+valueAfterSort[bPointer]==-valueAfterSort[i]:
                resultantValue=[valueAfterSort[aPointer],valueAfterSort[bPointer],valueAfterSort[i]]
                if resultantValue not in result:

                    result.append(resultantValue )
                aPointer+=1
                bPointer-=1
            

    return result
[[-2,-1,3],[-2,0,2],[-1,0,1]]          
listValue = [3,0,-2,-1,1,2]
print(threeSum(listValue))



""""aPointer=0
        bPointer=len(nums)-1
        nums=sorted(nums)
        result=[]
        for i in range(len(nums)):
            aPointer=i+1
            bPointer=len(nums)-1
            while aPointer<bPointer:
                valueToAdded=nums[aPointer]+nums[bPointer]
                if valueToAdded==-nums[i]:
                    finalVal=[nums[i],nums[aPointer],nums[bPointer]]
                    if finalVal not in result:
                        result.append(finalVal)
                    aPointer+=1
                    bPointer-=1
                elif valueToAdded>-nums[i]:
                    bPointer-=1
                elif valueToAdded<-nums[i]:
                    aPointer+=1
        return result"""