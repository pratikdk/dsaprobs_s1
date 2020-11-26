def sortColors(nums):
    red, white, blue = 0, 0, len(nums)-1
    while white <= blue:
        if nums[white] == 0: # Red
            nums[red], nums[white] = nums[white], nums[red]
            white += 1
            red += 1
        elif nums[white] == 1: # White
            white += 1
        else: # Blue
            nums[white], nums[blue] = nums[blue], nums[white]
            blue -= 1
    return nums


data = [
    [2,0,2,1,1,0],
    [2,0,1],
    [0],
    [1]
]

for test_list in data:
    print(sortColors(test_list))
