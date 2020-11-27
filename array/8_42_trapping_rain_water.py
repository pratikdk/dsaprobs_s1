# def trap(heights):
#     edge_a, edge_b = -1, -1
#     last_max = -1
#     trap_amt = 0
#     for i, height in enumerate(heights):
#         if edge_a < 0 and height > 0:
#             edge_a = i # height
#         else:
#             if height >= heights[last_max]:
#                 last_max = i
#             if height >= heights[edge_a] or i == len(heights)-1:
#                 if heights[last_max] >= heights[edge_a]:
#                     edge_b = i
#                 else:
#                     edge_b = last_max
#                 blocks = sum(heights[edge_a+1:edge_b])
#                 print("edge_a:", (i, edge_a, heights[edge_a]))
#                 print("edge_b:", (i, edge_b, heights[edge_b]))
#                 print("last_max", last_max)
#                 print()
#                 if edge_b-edge_a > 1:
#                     trap_amt += min(heights[edge_a], heights[edge_b]) * ((edge_b-1)-edge_a) - blocks
#                     #print(i, "YES", min(heights[edge_a], heights[edge_b]) * ((edge_b-1)-edge_a))
#                 blocks = 0
#                 edge_a = edge_b
#                 edge_b = -1
#                 last_max = -1
#     return trap_amt

# def trap(heights):
#     edge_a, temp_edge = -1, -1
#     final_amt = 0
#     buffer_amt = 0
#     for i, height in enumerate(heights):
#         if edge_a < 0 and height > 0:
#             edge_a = i # height
#             print("edge_a:", (edge_a, heights[edge_a]))
#         else:
#             #print("edge_b:", (i, i, heights[i]))
#             if height >= heights[edge_a]:
#                 print("idx:", i, "edge_a:", (edge_a, heights[edge_a]), "edge_b:", (i, heights[i]))
#                 final_amt += min(heights[edge_a], height) * ((i-1)-edge_a) - sum(heights[edge_a+1:i])
#                 print("edge_b added:", min(heights[edge_a], height) * ((i-1)-edge_a) - sum(heights[edge_a+1:i]))
#                 edge_a = i
#                 temp_edge = -1
#                 buffer_amt = 0
#             else:
#                 amt = 0
#                 if temp_edge > 0 and height <= heights[temp_edge]:
#                     amt = min(heights[temp_edge], height) * ((i-1)-temp_edge) - sum(heights[temp_edge+1:i])
#                     buffer_amt += amt
#                     print("idx:", i, "temp_edge:", (temp_edge,heights[temp_edge]), "amt:", amt,"heights:", heights[temp_edge+1:i])
#                 else:
#                     amt = min(heights[edge_a], height) * ((i-1)-edge_a) - sum(heights[edge_a+1:i])
#                     buffer_amt = amt
#                     print("idx:", i, "edge_a:", (edge_a,heights[edge_a]), "amt:", amt,"heights:", heights[edge_a+1:i])
#                 if (temp_edge > 0 and height >= heights[temp_edge]) or temp_edge < 0:
#                      temp_edge = i
#                      print("temp_edge:",(temp_edge,heights[temp_edge]))
#     if buffer_amt > 0:
#         final_amt += buffer_amt
#     return final_amt

def trap(heights):
    left = 0
    right = len(heights)-1
    leftmax = 0
    rightmax = 0
    ans = 0
    while left < right:
        if heights[left] < heights[right]: # consider left edge
            if heights[left] >= leftmax:
                leftmax = heights[left]
            else:
                ans += leftmax - heights[left]
            left += 1
        else: # consider left edge
            if heights[right] >= rightmax:
                rightmax = heights[right]
            else:
                ans += rightmax - heights[right]
            right -= 1
    return ans


data = [
    [4, 0, 3, 1, 2],
    [4,2,0,3,2,5],
    [0,1,0,2,1,0,1,3,2,1,2,1],
    [5, 4, 1, 2],
    [4,9,4,5,3,2],
    [4, 3, 1, 2]
]
for test_list in data:
    print(trap(test_list))
