def CandyCrush(candies):
        #First Cheack the rows
        crush=True
        column=len(candies[0])
        row=len(candies)
        for col in range(column):
            for rows in range(row-2):
            
            #-2 Because I have To check 3 Combinations
                candy1=abs(candies[rows][col])
                candy2=abs(candies[rows+1][col])
                candy3=abs(candies[rows+2][col])
                if candy1==candy2 and candy2==candy3 and candy1!=0:
                    candies[rows][col]=-candy1
                    candies[rows+1][col]=-candy2
                    candies[rows+2][col]=-candy3
                    crush=False
        
        for rows in range(row):
            for col in range(column-2):
                candy1=abs(candies[rows][col])
                candy2=abs(candies[rows][col+1])
                candy3=abs(candies[rows][col+2])
                if candy1==candy2 and candy2==candy3 and candy1!=0:
                    candies[rows][col]=-candy1
                    candies[rows][col+1]=-candy2
                    candies[rows][col+2]=-candy3
                    crush=False

        if crush==False:
            for col in range(column):
                needToSwap=len(candies)-1
                for rows in range(row-1,-1,-1):
                    if candies[rows][col]>0:
                        candies[needToSwap][col]=candies[rows][col]
                        needToSwap-=1
                for zero in range(needToSwap,-1,-1):
                    candies[zero][col]=0
       

        if crush==False:
            CandyCrush(candies)
        else:
            print(candies)



board =[[110,5,112,113,114],[210,211,5,213,214],[310,311,3,313,314],[410,411,412,5,414],[5,1,512,3,3],[610,4,1,613,614],[710,1,2,713,714],[810,1,2,1,1],[1,1,2,2,2],[4,1,4,4,1014]]

CandyCrush(board)
