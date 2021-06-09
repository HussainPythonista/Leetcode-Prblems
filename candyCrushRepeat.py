def candyCrush(candies):
    forRow=len(candies)
    forColumns=len(candies[0])
    crush=True
    #for cheack three three Pairs in rows
    for row in range(forRow):
        for col in range(forColumns-2):
        
            candy1=abs(candies[row][col])
            candy2=abs(candies[row][col+1])
            candy3=abs(candies[row][col+2])
            if candy1==candy2 and candy2==candy3 and candy1!=0:
                candies[row][col]=-candy1
                candies[row][col+1]=-candy2
                candies[row][col+2]=-candy3
                crush=False
    
    for col in range(forColumns):
        for row in range(forRow-2):
        
            candy1=abs(candies[row][col])
            candy2=abs(candies[row+1][col])
            candy3=abs(candies[row+2][col])
            if candy1==candy2 and candy2==candy3 and candy1!=0:
                candies[row][col]=-candy1
                candies[row+1][col]=-candy2
                candies[row+2][col]=-candy3
                crush=False
    if crush==False:
        for col in range(forColumns):
            needToSwap=len(candies)-1
            for row in range(len(candies)-1,-1,-1):
                if candies[row][col]>0:
                    candies[needToSwap][col]=candies[row][col]
                    needToSwap-=1
            for crush in range(needToSwap,-1,-1):
                    candies[crush][col]=0
            
    if crush==True:
        print(candies)
    else:
        candyCrush(candies)
candies=[[110,5,112,113,114],
[210,211,5,213,214],
[310,311,3,313,314],
[410,411,412,5,414],
[5,1,512,3,3],
[610,4,1,613,614],
[710,1,2,713,714],
[810,1,2,1,1],
[1,1,2,2,2],
[4,1,4,4,1014]]
candyCrush(candies)