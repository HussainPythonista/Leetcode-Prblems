
result=[]
def allPosiblities(listValue,result,bucket):
    print(bucket)
    data="" .join(bucket)
    result.append(data)
    if len(listValue)<len(bucket):
        #print(bucket)
        
        #
        return
    for i in range(len(listValue)):
        val=listValue.pop(0) 
        bucket.append(val)
        allPosiblities(listValue,result,bucket)
        listVal.append(bucket.pop())
    return listVal
listVal=["1","2"]
result=[]
bucket=[]
allPosiblities(listVal,result,bucket)
def decodeWays(possiblities):
    for i in range(1,27):
        print(i)

#decodeWays(result)
print(result)