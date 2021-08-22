def permutation(listValue,bucket,numberOfValues,resultIwant):
    if len(bucket)==numberOfValues:
        resultIwant.append(bucket.copy())
        return
    else:
        for _ in range(len(listValue)):
            tempVal=listValue.pop(0)
            bucket.append(tempVal)
            permutation(listValue,bucket,numberOfValues,resultIwant)
            bucketPop=bucket.pop()
            listValue.append(bucketPop)
    return resultIwant
def nextPermutation(listValue):
    resultIwant=[]
    bucket=[]
    numberOfValues=len(listValue)
    tempListValue=list(sorted(listValue))
    #print(tempListValue)
    forPermute=permutation(tempListValue,bucket,numberOfValues,resultIwant)
    #print(forPermute)
    if forPermute[-1]==listValue:
        return forPermute[0]
    else:
        for i in range(len(forPermute)):
            if forPermute[i]==listValue:
                return forPermute[i+1]
    

listValue=[1,1,5]
print(nextPermutation(listValue))