def CandyCrush(candies):
        #First Cheack the rows
        for col in range(len(candies[0])):
            for row in range(len(candies)-2):
                num1=abs(candies[row][col])


                num2=abs(candies[row+1][col])
                num3=abs(candies[row+2][col])
                if num1==num2 and num2==num3 and num1!=0:
                    candies[row][col]=-num1
                    candies[row+1][col]=-num2
                    candies[row+2][col]=-num3
        
        
        for row in range(len(candies)):# Checking column if 3 consequtive elements are same then we put -num to it
            for col in range(len(candies[0])-2):
                num1=abs(candies[row][col])
                num2=abs(candies[row][col+1])
                num3=abs(candies[row][col+2])
                if num1==num2 and num2==num3 and num1!=0:
                    candies[row][col]=-num1
                    candies[row][col+1]=-num2
                    candies[row][col+2]=-num3
        #print(candies)
        crush=False
        for column in range(len(candies[0])):
            swap=len(candies)-1
            for row in range(len(candies)-1,-1,-1):
                if candies[row][column]>0:
                    candies[swap][column]=candies[row][column]
                    swap-=1
            for swapable in range(swap,-1,-1):
                candies[swapable][column]=0
        print(candies)

board =[
[110,5,112,113,114],
[210,211,5,213,214],
[310,311,3,313,314],
[410,411,412,5,414],
[5,1,512,3,3],
[610,4,1,613,614],
[710,1,2,713,714],
[810,1,2,1,1],
[1,1,2,2,2],
[4,1,4,4,1014]
]

CandyCrush(board)
