# def n_sum(array):
#     n = 3
#     res = []
#     if len(array) < n: return res
#     heads = [0]*(n-1)
#     for i in range(n-1, len(array)):
#         for b in range(len(heads)):
#             heads[b] = b
#         slider = len(heads)-1
#         while slider >= 0 and heads[slider] < i:
#             comb = sorted(tuple(array[j] for j in heads) + (array[i],))
#             if (sum(comb) == 0) and (comb not in res):
#                 res.append(comb)
#             heads[slider] += 1
#             if (heads[slider] == i) or ((slider < (n-2)) and (heads[slider] == heads[slider+1])):
#                 slider -= 1
#     return res

def threeSum(array):
    res = []
    array.sort()
    for i, a in enumerate(array):
        if i > 0 and a == array[i-1]:
            continue
        l, r = i+1, len(array)-1
        while l < r:
            threesum = a + array[l] + array[r]
            if threesum > 0: # Reduce the sum
                r -= 1
            elif threesum < 0: # Increase the sum
                l += 1
            else:
                res.append([a, array[l], array[r]])
                l += 1
                while array[l] == array[l-1] and l < r:
                    l += 1
    return res

data = [
    [-1,0,1,2,-1,-4],
    [2, -2, 0],
    [2, -2, 1],
    [],
    [0],
    [5,2,-2,-1, 4],
    [-1, 0, 1, 2, 3, 4]
]

for test_list in data:
    print(threeSum(test_list))
