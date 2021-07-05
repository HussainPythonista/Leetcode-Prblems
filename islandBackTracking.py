island = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 1],
    [1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0]
]
grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
count=0
def findingIsland(row,column,island,visited):
    
    if row<0 or column<0 or row>len(island)-1 or column>len(island[0])-1:
        return

    elif island[row][column]=="1" and visited[row][column]!=True:
        
        visited[row][column]=True
        
        findingIsland(row-1,column,island,visited)
        findingIsland(row+1,column,island,visited)
        findingIsland(row,column+1,island,visited)
        findingIsland(row,column-1,island,visited)
        
        return 1
    
def islandToFind(row,column,island):
    visited = [[False for i in range(len(grid[0]))] for j in range(len(island))]
    count=0
    for i in range(len(island)):
        for j in range(len(island[0])):
            if grid[i][j]=="1" and visited[i][j]!=True:
                row=i
                column=j
                count+=(findingIsland(row,column,grid,visited))
    return count
                    
    
row=0
column=0
print(islandToFind(row,column,grid))
#print(findingIsland(row,column))

