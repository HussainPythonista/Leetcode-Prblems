#arr = [7,7,7,7,7,7,7,7,7,7,7,7]
#arr = [3,3,3,3,5,5,5,2,2,7]
#arr = [1,9]
#arr = [1000,1000,3,7]
#arr = [1,2,3,4,5,6,7,8,9,10]
#arr=[2,28,92,30,100,52,28,48,91,27,66,19,11,53,91,95,74,51,65,65,96,81,21,55,98,3,2,89,99,57,78,34,50,2,57,76,23,90,89,36,53,22,73,59,95,45]
arr=[72,18,36,6,12,97,41,82,44,75,82,42,75,48,63,9,61,50,11,91,24,26,3,65,31,67,15,76,54,59,4,27,33,26,17,60,100,19,90,6,80,82,48,70,85,99,69,2,78,94,15,29,75,17,9,79,99,88,26,73,88,100,9,95,2,56,63,31,25,40,8,100,56,44,36,42,21,96,63,38,96,78,60,22,21,81]
def numberOfOccurance(arr):
    dictvalue = {}
    for i in range(len(arr)):
        if arr[i] in dictvalue:
            dictvalue[arr[i]]+=1
        else:
            dictvalue[arr[i]]=1
    print(dictvalue)
    listValue=[]
    for key,values in dictvalue.items():
        listValue.append(values)
    return list(sorted(listValue,reverse=True))

def reducedHalf(arr):
    halfOfArray = len(arr)//2
    value = numberOfOccurance(arr)
    
    summedValue=sum(value)
   
    count=0
    for i in range(len(value)):
        
        summedValue-=value[i]
        #print(summedValue)
        count+=1
        if summedValue<=halfOfArray:
            
            return (count)
        

print(reducedHalf(arr))
