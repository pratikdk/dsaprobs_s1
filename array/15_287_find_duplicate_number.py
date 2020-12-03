# def findDuplicate(nums):
#     actual_sum = 0
#     max = 0
#     for num in nums:
#         actual_sum += num
#         if max < num:
#             max = num
#     expected_sum = (max*(max+1))/2
#     return actual_sum-expected_sum


def findDuplicate(nums):
    map = {}
    for num in nums:
        if num in map:
            return num
        else:
            map[num] = 1
        return -1

    actual_sum = 0
    max = 0
    for num in nums:
        actual_sum += num
        if max < num:
            max = num
    expected_sum = (max*(max+1))/2
    return actual_sum-expected_sum

data = [
    [1,3,4,2,2],
    [3,1,3,4,2],
    [1,1],
    [1,1,2]
]

for test_list in data:
    print(findDuplicate(test_list))
