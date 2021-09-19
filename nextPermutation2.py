num=[4,2,0,2,3,2,0]
#num=[6,2,1,5,4,3,0]
#num=[1,2,4,3]
num=[2,3,4,2]
#num=[2,4,3,2]
#num=[1,2,3,4,5,4,2]
#[4,2,0,3,0,2,2]
num=[1,3,2]
def nextPermutation(num):
    last=len(num)-1
    peak=num[last]
    indexOfPeak=0
    for i in range(last,-1,-1):
        if (num[i]>num[i-1]):
            peak=(num[i])
            indexOfPeak=i
            break
    #print(indexOfPeak)
    immediateNextValue=0
    immediateLesserIndex=0
    for i in range(indexOfPeak,-1,-1):
        if num[i]<peak:
            immediateNextValue=num[i]
            immediateLesserIndex=i
            break
    print(immediateLesserIndex)
    for tempPeak in range(indexOfPeak,len(num)):
        if num[tempPeak]<peak and num[tempPeak]>immediateNextValue:
            peak=(num[tempPeak])
            indexOfPeak=tempPeak
    #Swaping
    num[immediateLesserIndex],num[indexOfPeak]=num[indexOfPeak],num[immediateLesserIndex]

    for i in range(immediateLesserIndex+1,len(num)):
        for j in range(i+1,len(num)):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
    print(num)
nextPermutation(num)
