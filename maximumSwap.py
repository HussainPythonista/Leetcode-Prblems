def MaximumSwap(nums):
    strValue=str(nums)
    listValue=[]
    for i in range(len(strValue)):
        listValue.append(int(strValue[i]))
    dpMaximumValue=-1
    dbMaximumOfI=[-1 for i in range(len(listValue))]
    maxI=0
    for i in range(len(listValue)-1,-1,-1):
        if dpMaximumValue<listValue[i]:
            dpMaximumValue=listValue[i]
            maxI=i
        dbMaximumOfI[i]= maxI
    
    for i in range(len(listValue)):
        
        if listValue[i]<listValue[dbMaximumOfI[i]]:
            listValue[i],listValue[dbMaximumOfI[i]]=listValue[dbMaximumOfI[i]],listValue[i]
    print(listValue)
#num = 2736#7236
num=98368#98863
#num=120#210
MaximumSwap(num)