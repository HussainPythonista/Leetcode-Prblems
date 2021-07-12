n = 1  # Number of Bits


def grayCode(n):  # Im solving this Question by using BIt Manupulation
    
    if n>1:
        i = 0
        stop = True
        answerIWant=[]
        while stop:
            
            binaryValues = bin(i)
            #print(binaryValues)
            binaryValues=binaryValues[2:]
            if i==0:
                binaryValues="00"
            elif i==1:
                binaryValues="01"
            if len(binaryValues) <= n:
                
                #Conditions of Grey Code
                #1>Add the first value to conditions
                #2> If the next Values are same add 0 else thhe next Values are not equal add 1
                addedValue=binaryValues[0]
                for needToBeGrayCode in range(1,len(binaryValues)):
                    if binaryValues[needToBeGrayCode-1]==binaryValues[needToBeGrayCode]:
                        addedValue+="0"
                    elif binaryValues[needToBeGrayCode-1]!=binaryValues[needToBeGrayCode]:
                        addedValue+="1"
                addedValue=int(addedValue,2)
                answerIWant.append(addedValue)
                
                    
            else:
                stop = False
            i += 1
    else:
        answerIWant=[0,1]
    return answerIWant


#same Gray code in BackTracking Algorithm
result=[]
def grayCodeBackTracking()