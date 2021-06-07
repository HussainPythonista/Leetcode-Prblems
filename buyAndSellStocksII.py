#prices = [7,1,5,3,6,4]
from sys import api_version


prices=[1,2,3,4,5]
"""
maxProfit=0
for i in range(1,len(prices)):
    
    if prices[i]>prices[i-1]:
        maxProfit+= prices[i]-prices[i-1]
print(maxProfit)"""

def hillValleyApproach(prices):
    hill=prices[0]
    valley=prices[0]
    maxValue=0
    for i in range(1,len(prices)):
        aPointer=i+1
        if prices[i]>prices[i-1] :
            maxValue+=prices[i]-prices[i-1]

    print(maxValue)
prices = [1,2,3,4,5]
hillValleyApproach(prices)





    

    
    
    

    

    
    
    