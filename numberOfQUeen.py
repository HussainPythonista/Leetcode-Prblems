answer = []
def isSafe(row, col, matrix, N):

    dummyROw = row
    dummyCol = col
    while col>=0 and row>=0:
        if matrix[row][col] == 1:
            return False
        row-=1
        col-=1
    col = dummyCol
    row = dummyROw
    while col>=0:
        if matrix[row][col] == 1:
            return False
        col-=1
        
    col = dummyCol
    row = dummyROw

    while row<N and col>=0:
        if matrix[row][col] == 1:
            return False
        row+=1
        col-=1
    return True
print(answer)
visited=False
def nNumberOfQueens(matrix, col, N):
    global answer,visited
   
    if col == N:
        return True
    for i in range(N):
        if isSafe(i, col, matrix, N) == True:     
                            
            matrix[i][col] = 1
            if nNumberOfQueens(matrix, col+1, N)==True:
                return True
            matrix[i][col] = 0
    return answer
matrix = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0],
]
N = len(matrix)

col = 0
if nNumberOfQueens(matrix, col, N)==True:
    
    print(matrix)
