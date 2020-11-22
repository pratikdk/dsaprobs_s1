def first_unique(s):
    if s is None or len(s) < 1: return -1
    map = {}
    index = 0
    for i, char in enumerate(s):
        if char not in map:
            map[char] = 0
        map[char] += 1
        while map[s[index]] > 1:
            index += 1
            if index >= len(s):
                index = -1
                break
            elif index > i:
                break
    return index

data = [
    "lool",
    "love",
    "lovel",
    "leetcode",
    "loveleetcode",
    " ",
    "",
    "ll",
    "loolc",
    "loodlc",
    ""
]

for test_string in data:
    print(first_unique(test_string))
