
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
listValue=[]
def path(movingIndexRight,MovingIndexDown,finalRight,FinalDown,moveSide):
  global listValue
  if movingIndexRight==finalRight and MovingIndexDown==FinalDown:
    listValue.append(moveSide)
  elif movingIndexRight>finalRight or MovingIndexDown>FinalDown:
    return 
  else:
    path(movingIndexRight+1,MovingIndexDown,finalRight,FinalDown,moveSide+"R")
      

    path(movingIndexRight,MovingIndexDown+1,finalRight,FinalDown,moveSide+"D")
   
  return listValue
movingIndexRight,MovingIndexDown,finalRight,FinalDown,moveSide=0,0,3,3,""



listValue=[]
performOperation=True
def reachingPath(nums,start,end,targetRow,targetCol,side,visited):
  global listValue,performOperation
  if start<0 or end<0:
    performOperation=False
    return
  elif start>targetRow or end>targetCol:
    performOperation=False
    return
  elif nums[start][end]==0:
    performOperation=False
    return
  elif visited[start][end]==True:
    performOperation=False
    return
  if start==targetRow and end ==targetCol:
    listValue.append([side])
  if  performOperation==True:
      visited[start][end]=True
      reachingPath(nums,start,end-1,targetRow,targetCol,side+"U",visited)#Top move
      reachingPath(nums,start+1,end,targetRow,targetCol,side+"R",visited)#Right move
      reachingPath(nums,start,end+1,targetRow,targetCol,side+"D",visited)#Down Move
      reachingPath(nums,start-1,end,targetRow,targetCol,side+"L",visited)#left Move
   
  return listValue
nums=[[1,1,1,1],
      [1,1,1,1],
      [1,0,1,1],
      [1,1,0,1]]
visited=[[False for j in range(len(nums[0]))]for i in range(len(nums))]
start,end,targetRow,targetCol,side=0,0,3,3,""
print(reachingPath(nums,start,end,targetRow,targetCol,side,visited))