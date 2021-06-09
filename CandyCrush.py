board=[[110,5,112,113,114],
        [210,211,5,213,214],
        [310,311,3,313,314],
        [410,411,412,5,414],
        [5,1,512,3,3], 
        [610,4,1,613,614],
        [710,1,2,713,714],
        [810,1,2,1,1],
        [1,1,2,2,2],
        [4,1,4,4,1014]]
def CandyCrush(board):
    #For Crushing Row
    crush=True
    for row  in range(len(board)):
        for column in range(len(board[0])-2):
            nums1=abs(board[row][column])
            nums2=abs(board[row][column+1])
            nums3=abs(board[row][column+2])
            if nums1==nums2 and nums2==nums3 and nums1!=0:
                board[row][column]=-nums1
                board[row][column+1]=-nums2
                board[row][column+2]=-nums3
                crush=False
    #For Crushing Column
    for column  in range(len(board[0])):
        for row  in range(len(board)-2):
            num1=abs(board[row][column])
            num2=abs(board[row+1][column])
            num3=abs(board[row+2][column])
            if num1==num2 and num2==num3 and num1!=0:
                board[row][column]=-num1
                board[row+1][column]=-num2
                board[row+2][column]=-num3
                crush=False
    
    #For Changing Gravity
    if crush==False:
        for column in range(len(board[0])):
            swapAbleIndex=len(board)-1
            for row in range(len(board)-1,-1,-1):
                if board[row][column]>0:
                    board[swapAbleIndex][column]=board[row][column]
                    swapAbleIndex-=1
            for row in range(swapAbleIndex,-1,-1):
                    board[row][column]=0
    if crush==True:
        print(board)
    else:
        CandyCrush(board)        
    
    
    
CandyCrush(board)

"""
OutPut

[[0,0,0,0,0],
[0,0,0,0,0],
[0,0,0,0,0],
[110,0,0,0,114],
[210,0,0,0,214],
[310,0,0,113,314],
[410,0,0,213,414],
[610,211,112,313,614],
[710,311,412,613,714],
[810,411,512,713,1014]]
"""
