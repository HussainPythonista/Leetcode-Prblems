island = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0]
]
visited = [[False for i in range(len(island[0]))] for j in range(len(island))]
zerothPosition = 0


def findingIslendIn2DArray(nums, rightMove, downMove,counter):
    global visited
    if rightMove < 0 or downMove < 0:
        return 0
    elif rightMove >= len(nums[0])-1 or downMove >= len(nums)-1:
        return 0
   
    elif visited[rightMove][downMove] == True:
        return 0
    else:
        visited[rightMove][downMove] = True
        findingIslendIn2DArray(nums, rightMove+1, downMove,counter)
        findingIslendIn2DArray(nums, rightMove-1, downMove,counter)
        findingIslendIn2DArray(nums, rightMove, downMove+1,counter)
        findingIslendIn2DArray(nums, rightMove, downMove-1,counter)
        return 1
def Findisland(island):
    
    counter = 0
    for i in range(len(island)):
        for j in range(len(island[0])):
            if island[i][j] == 1:
                
                val = findingIslendIn2DArray(island, i, j,counter)
                counter+=val
    print(counter)
Findisland(island)


print(2%10)