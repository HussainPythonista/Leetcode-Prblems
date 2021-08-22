result=[]
def permutation(Array,bucket,k):
    global result
    if len(bucket)==k:
        result.append(bucket.copy())
        return
    #else:
    for _ in range(len(Array)):
            currentVal=Array.pop(0)
           # currentVal.append
            bucket.append(currentVal)
            #print(bucket)
            permutation(Array,bucket,k)
            replaceVal=bucket.pop()
            Array.append(replaceVal)
    return Array
Array=[1,1,3]
k=len(Array)
butket=[]
permutation(Array,butket,k)
answerWithoutDuplicates=[]
for i in range(len(result)):
    if result[i] not in answerWithoutDuplicates:
        answerWithoutDuplicates.append(result[i])
print(answerWithoutDuplicates)