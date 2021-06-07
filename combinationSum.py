
print("Hello")

candidates = [2,3,6,7]
target = 7
listValue=[]
def PathFinding(startRow,startColumn,targetRow,targetColumn,result):
    global listValue
    if startColumn>targetColumn or startRow>targetRow:
        return
    if startColumn==targetColumn and startRow==targetRow:
        listValue.append([result])
    if (startColumn==0 and startRow==1) or (startColumn==2 and startRow==1):
        return
    PathFinding(startRow+1,startColumn,targetRow,targetColumn,result+"R")#Row Increment
    PathFinding(startRow,startColumn+1,targetRow,targetColumn,result+"D")#For Column Tracing
    PathFinding(startRow-1,startColumn,targetRow,targetColumn,result+"L")#Row Increment
    PathFinding(startRow,startColumn-1,targetRow,targetColumn,result+"T")
    return listValue[0]

targetRow=3
targetColumn=3
startRow=0
startColumn=0
result=""
universalResult=[]
print(PathFinding(startRow,startColumn,targetRow,targetColumn,result))
def CombinationSum(listValue,Target,Path,index):
    global universalResult
    if Target<0:
        return 
    if Target==0:
        universalResult.append([ele for ele in Path])
        
    else:
        for i in range(index,len(listValue)):
            Path.append(listValue[i])
            CombinationSum(listValue,Target-listValue[i],Path,i)
            Path.pop()
    return universalResult
Path=[]
candidates.sort()
print(universalResult)
