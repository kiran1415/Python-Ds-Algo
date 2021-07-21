def maxProfit(prices):
    min_buy = float('inf')
    max_profit = 0
    pist = 0
    for item in prices:
        if item<min_buy:
            min_buy = item
        pist = item - min_buy
        if pist>max_profit:
            max_profit = pist
    return max_profit

prices = [7,1,5,3,6,4]
print("ans:",maxProfit(prices))