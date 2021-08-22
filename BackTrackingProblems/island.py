def backTracking(visited,array,left,column):
    if left<0 or left>=len(array[0]) or column<0 or column>len(array):
        return
    
    
    if visited[left][column]==False and array[left][column]==1:
        visited[left][column]=True
        backTracking(visited,array,left+1,column)
        backTracking(visited,array,left-1,column)
        backTracking(visited,array,left,column+1)
        backTracking(visited,array,left,column-1)
        return 1
def island(array,visited):
    count=0
    for i in range(len(array)):
        for j in range(len(array[0])):

            if array[i][j]==1 and visited[i][j]==False:
                
                count+=(backTracking(visited,array,i,j))
    return count

array=[
    [1,1,1,0],
    [0,0,0,0],
    [1,1,0,0],
    [1,1,0,0],]

visited=[[False for _ in range(len(array))] for _ in range(len(array[0]))]
print(visited)
     
island(array,visited)