# def missingNumber(nums):
#     min = 0
#     max = 0
#     for n in nums:
#         if n < min:
#             min = n
#         if n > max:
#             max = n
#     minsum = (min*(min+1))/2
#     maxsum = (max*(max+1))/2
#     return (maxsum-minsum) - sum(nums)

def missingNumber(nums):
    min = 0
    max = len(nums)
    maxsum = (max*(max+1))/2
    return (maxsum) - sum(nums)

data = [
    [3,0,1],
    [9,6,4,2,3,5,7,0,1],
    [0,1],
    [0]
]

for test_list in data:
    print(missingNumber(test_list))
