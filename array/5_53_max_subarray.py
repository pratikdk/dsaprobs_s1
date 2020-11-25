def maxSubArray(nums):
    max_sum = nums[0]
    max = []
    buffer = []
    for i, num in enumerate(nums):
        buffer.append(num)
        buffer_sum = sum(buffer)
        if max_sum < buffer_sum: max_sum = buffer_sum
        #print(buffer, buffer_sum, max_sum)
        if buffer_sum <= 0 or i == len(nums)-1:
            if buffer_sum <= 0:
                buffer.pop()
                #print("Here is max:", max, max_sum, sum(buffer), sum(max))
            if sum(buffer) >= sum(max):
                max = buffer
                buffer = []
            else: buffer = []
    return max_sum

data = [
    [-2,1,-3,4,-1,2,1,-5,4],
    [2, -2],
    [2, -2, 3],
    [2, 0, 3],
    [1],
    [0],
    [-1],
    [-2147483647],
    [-1,1,-3,-2,2,-1,-2,1,2,-3], #3
    [-1,-6,-9,4,-8,5,-4,2,-1,1,-8,0,1,3,1]
]

for test_list in data:
    print(maxSubArray(test_list))
