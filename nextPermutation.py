def nextPermutation(num):
    head=0
    last=len(num)-1
    i=last
    needTochange=0
    while i>=0:
    
        for j in range(i,-1,-1):
            if num[i]>num[j]:
                num[i],num[j]=num[j],num[i]
                #print(i)
                needTochange=j
                return needTochange
        i-=1
    """else:
        for i in range(len(num)):
            for j in range(i+1,len(num)):
    
                if num[i]>num[j]:

                    num[i],num[j]=num[j],num[i]
        return 0"""
num=[4,2,0,2,3,2,0]
#[4,2,0,3,0,2,2]
tempAnswer=nextPermutation(num)
for i in range(tempAnswer+1,len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:

            num[i],num[j]=num[j],num[i]
print(num)