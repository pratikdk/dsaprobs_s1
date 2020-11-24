def twoSum(numbers, target):
    l = 0, r = len(numbers):
    while l < r:
        two_sum = numbers[l] + numbers[r]
        if two_sum > target:
            r -= 1
        elif twosum < target:
            l += 1
        else:
            return [l+1, r+1]
    return []
