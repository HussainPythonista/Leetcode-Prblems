from ast import Num

#num=9973
num=2736
num =98368
num=120
def swap(db,listValue):
    for i in range(len(listValue)):
        currentMax=listValue[db[i]]
        currentNum=i
        if currentMax>currentNum:
            temp=listValue[i]
            listValue[i]=listValue[db[i]]
            listValue[db[i]]=temp
            break
    print(listValue)
    
def maximumSwap(listValue):
    tableForDp=[-1 for i in range(len(listValue))]
    maximumI=-1
    maxValue=-1
    for i in range(len(listValue)-1,-1,-1):
        if listValue[i]>maxValue:
            maxValue=listValue[i]
            maximumI=i
        tableForDp[i]=maximumI
    for i in range(len(listValue)):
        currentMax=listValue[tableForDp[i]]
        print(currentMax)
        currentNum=listValue[i]
        if currentMax>currentNum:
            temp=listValue[i]
            listValue[i]=listValue[tableForDp[i]]
            listValue[tableForDp[i]]=temp
            break
    strValue=[]
    for i in range(len(listValue)):
        strValue.append(str(listValue[i]))
    forReturn="".join(strValue)
    return int(forReturn)
def changeTheValuesAsMyConvience(nums):
    stringvalue=str(nums)
    listValue=[]
    for x in range(len(stringvalue)):
        listValue.append(int(stringvalue[x]))
    return maximumSwap(listValue)
print(changeTheValuesAsMyConvience(num))