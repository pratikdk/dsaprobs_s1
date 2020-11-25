# def best_buy(prices):
#     min_i, max_i = 0, 0
#     abs_min_i = 0
#     for i, curr_price in enumerate(prices):
#         if curr_price <= prices[abs_min_i]:
#             abs_min_i = i
#         if i < max_i and curr_price < prices[min_i]:
#             min_i = i
#         if curr_price > prices[max_i]:
#             max_i = i
#             if prices[abs_min_i] < prices[min_i]:
#                 min_i = abs_min_i
#     return ([min_i, max_i], [prices[min_i], prices[max_i]], prices[max_i]-prices[min_i])

# def best_buy(prices):
#     min_i, max_i = 0, 0
#     buffer_i = 0
#     for i, curr_p in enumerate(prices):
#         if (curr_p < prices[min_i]): # curr_p is less
#             if min_i < max_i:
#                 min_i = i # update min_i
#             else: # possible mininum, save the index in buffer
#                 buffer_i = i
#
#         if (curr_p > prices[max_i]) or (buffer_i > max_i): # curr_p is more
#             if curr_p > prices[min_i]:
#                 max_i = i
#                 if buffer_i < max_i:
#                     min_i = buffer_i
#             else:
#                 if buffer_i > min_i and min_i == 0:
#                     min_i = buffer_i
#                     max_i = min_i
#                 else:
#                     max_i = min_i
#     return ([min_i, max_i], [prices[min_i], prices[max_i]], prices[max_i]-prices[min_i])

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0
    for i, price in enumerate(prices):
        if price < min_price:
            min_price = price
        elif (price-min_price) > max_profit:
            max_profit = price-min_price
    return max_profit

# Below keeps valid min and max prices
# def maxProfit(prices):
#     old_min = 0
#     min_i, max_i = 0, 0
#     min_price = float('inf')
#     max_profit = 0
#     min_after_max = False
#     for i, price in enumerate(prices):
#         if price < min_price:
#             old_min = min_price
#             min_price = price
#             min_i = i
#             if max_i < i:
#                 min_after_max = True
#         elif (price-min_price) > max_profit:
#             max_profit = price-min_price
#             max_i = i
#             old_min = min_price
#             min_after_max = False
#         if i == len(prices)-1:
#             if min_after_max:
#                 old_min = min_price
#                 max_i = min_i
#     #return [(old_min, prices[max_i]), prices[max_i]-old_min, max_profit]
#     return max_profit

data = [
    [7,2,6,1,9,1,8],
    [7,2,1,6,7,1,9,8],
    [1, 7, 1, 8, 2],
    [7,1,5,3,6,4],
    [7,6,4,3,1],
    [2, 3, 1, 4, 7]
]
for seq in data:
    print(maxProfit(seq))
