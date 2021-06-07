prices = [7,1,5,3,6,4]
def MaxProfit(prices):
    buy=prices[0]
    sell=0
    for i in range(len(prices)):
        buy=min(buy,prices[i])
        sell=max(sell,prices[i]-buy)
    print(sell)

print(MaxProfit(prices))
