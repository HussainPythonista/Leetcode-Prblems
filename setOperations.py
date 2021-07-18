def union(num1,num2):
    unionset=[]
    for i in range(len(num1)):
        for j in range(len(num2)):
            if num1[i]!=num2[j] and num1[i] not in unionset and num2[j] not in unionset:
                unionset.append(num1[i])
                unionset.append(num2[j])
    print(unionset)


num1=[2,3,4,2,1]
num2=[5,3,1,4,16]

def inTersection(num1,num2):
    intersection=[]
    for i in range(len(num1)):
        for j in range(len(num2)):
            if num1[i]==num2[j]:
                intersection.append(num2[j])
    return intersection


def findingMultipleMissingElement(nums):
    difference=nums[0]
    valuesWhichMissing=[]
    for i in range(len(nums)):
        if nums[i]-i!=difference:
            valuesWhichMissing.append(difference+i)
            difference=nums[i]-i

            
    print(valuesWhichMissing)
            



def findingMultipleMissingNumInUnsortedArray(nums):
    minimum=min(nums)
    maximum=max(nums)
    memoization=[0 for i in range(maximum)]
    memoization[-1]=1
    
    for i in range(len(nums)-1):
        dif=nums[i]
        memoization[dif]=1
    memoization= memoization[minimum:]
    for i in range(len(memoization)):
        if memoization[i]==0:
            print(i)


def duplicates(nus):
    withoutDuplicateduplicates=[]
    dup=[]
    numberOfTimes={}
    for i in range(len(nus)):
        if nus[i] not in withoutDuplicateduplicates:
            withoutDuplicateduplicates.append(nus[i])
            numberOfTimes[nus[i]]=1
        else:
            dup.append(nus[i])
            numberOfTimes[nus[i]]+=1
    print(dup,numberOfTimes)
nus=[3,2,1,3,1,4,3,7,3]

nums=[14,7,6,5,4,3,8,6,10,10,10,10,7,2,4,3,8,14]
def findDuplicatesWithDynamicProgramming(nums):
    minimum=min(nums)
    maximum=max(nums)
    memization=[0 for _ in range(maximum+1)]
    for i in range(len(nums)):
       memization[nums[i]]+=1
    memization=memization[minimum:]
    print(memization)


nums=[2,2]
def twoSum(nums,target):
    memoization={}
    for i in range(len(nums)):
        compliment=target-nums[i]
        if compliment not in memoization:
            memoization[nums[i]]=i
        else:
            print(memoization[compliment],i)
    
target=4
twoSum(nums,target)

def minMax(nums):
    maximumValue=nums[0]
    maximumOfMaximum=0

    minimumVal=nums[0]
    minimumOfMin=999999999999999999999999999999999
    for i in range(len(nums)-1):
        if nums[i+1]>nums[i]:
            maximumValue=nums[i+1]
            if maximumOfMaximum<maximumValue:
                maximumOfMaximum=maximumValue
        if nums[i+1]<nums[i]:
            minimumVal=nums[i+1]
            if minimumOfMin>minimumVal:
                minimumOfMin=minimumVal
        
    print(maximumOfMaximum,minimumOfMin)



