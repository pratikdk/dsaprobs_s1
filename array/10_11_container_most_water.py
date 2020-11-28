def maxArea(height):
    """
    :type height: List[int]
    :rtype: int
    """
    maxarea = 0
    l = 0
    r = len(height) - 1
    while(l < r):
        maxarea = max(maxarea, min(height[l], height[r]) * (r-l))
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return maxarea

data = [
    [1,1], #1
    [1,8,6,2,5,4,8,3,7], #49
    [4,3,2,1,4], #16
    [1,2,1] #2
]
for test_list in data:
    print(maxArea(test_list))
