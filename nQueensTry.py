def isSafe(board,row,col,N):
    dummyRow=row
    dummyCol=col

    row=dummyRow
    col=dummyCol
    while row>=0 and col>=0:
        if board[row][col]==1:
            return False
        row-=1
        col-=1
    
    row=dummyRow
    col=dummyCol
    while row<N and col>=0:
        if board[row][col]==1:
            return False
        row+=1
        col-=1
    row=dummyRow
    col=dummyCol
    while col>=0:
        if board[row][col]==1:
            return False
        #row+=1
        col-=1
    return True
answer=[]
def nQueens(board,col,N):
    global answer
    if col>=N:
        return True
    
    for i in range(N):
            
            if isSafe(board,i,col,N)==True:
                board[i][col]=1
                if nQueens(board,col+1,N)==True:

                    return True
                board[i][col]=0
    
N=
col=0
board=[[0 for _ in range(N)] for _ in range(N)]
nQueens(board,col,N)
print(board)