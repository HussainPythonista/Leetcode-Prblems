arrayValue=[-2,1,-3,4,-1,2,1,-5,4]

maxValue=arrayValue[0]#1
maxOfMaximum=0
for i in range(1,len(arrayValue)):
    maxValue=max(arrayValue[i],maxValue+arrayValue[i])
    maxOfMaximum=max(maxOfMaximum,maxValue)
print(maxOfMaximum)
    