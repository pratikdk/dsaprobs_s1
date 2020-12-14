def leastInterval(tasks, n):
    counts = [0]*26
    for task in tasks:
        char_no = ord(task) - ord('A')
        counts[char_no] += 1
    counts.sort()
    i = 25
    while i >= 0 and counts[i] == counts[25]:
        i -= 1
    return max(len(tasks), (counts[-1]-1) * (n+1) + (25 - i))



print(leastInterval(["A","A","A","B","B","B"], 2))
