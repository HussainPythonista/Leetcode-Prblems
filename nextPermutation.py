from typing import MutableMapping


def nextPermutation(num):
    head=0
    last=len(num)-1
    i=last
    while i>=0:
    
        for j in range(i,-1,-1):
            # print(num[j])
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
                needToFindPlace=j
                #print(i)
                #num=num
                #poped=num.pop(i)
                return (num,j)#,firstIndex)
    
                
           #num=num[:1]+sorted(num[1:])
           #print()
        else:
            return (num,0)
        i-=1
    """else:
        for i in range(len(num)):
            for j in range(i+1,len(num)):
                if num[i]<num[j]:
                    num[i],num[j]=num[j],num[i]
        print(True)
        return num"""
    #print(num[0])
num=[3,2,1]

tempAnswer=nextPermutation(num)
num=tempAnswer[0]
for i in range(tempAnswer[1]+1,len(tempAnswer[0])):
    for j in range(i,len(tempAnswer[0])):
        if num[i]>=num[j]:
                num[i],num[j]=num[j],num[i]
print(num)
print(tempAnswer)