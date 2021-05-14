# def maxProfit(prices):
#     min_price = float('inf')
#     max_profit = 0
#     n = len(prices)
#     for i, price in enumerate(prices):
#         if price < prices[i-1]: # Breakaway from loss
#             if min_price < prices[i-1]: # but firt Capture prof
#                 max_profit += prices[i-1]-min_price
#             min_price = price
#         if (i==n-1) and (price>min_price):
#             max_profit += price-min_price
#     return max_profit

def maxProfit(prices):
    if len(prices) < 1: return 0
    min_price = prices[0]
    max_profit = 0
    n = len(prices)
    for i, price in enumerate(prices):
        if i == 0: continue
        if price < prices[i-1]: # Breakaway from loss
            #if min_price < prices[i-1]: # but firt Capture prof
            max_profit += prices[i-1]-min_price
            min_price = price # reset minprice
        if (i==n-1) and (price>min_price): # last elem, caputre prof
            max_profit += price-min_price
    return max_profit

data = [
    [7,1,5,3,6,4],
    [1,2,3,4,5],
    [7,6,4,3,1],
    [7,1,5,0,3,6,2,8],
    [2, 4, 1],
    [5],
    [7,2,6,1,9,1,8],
    []
]

7
4
0
16
2
0
19
0

for seq in data:
    print(maxProfit(seq))
