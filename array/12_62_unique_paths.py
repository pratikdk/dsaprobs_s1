def uniquePaths(m, n):
    matrix = []
    matrix.append([1]*n)
    for i in range(1, m):
        row = [0]*n
        for j in range(n):
            if j == 0: row[j] = 1
            else: row[j] = row[j-1] + matrix[i-1][j]
        matrix.append(row)
    return matrix[-1][-1]

data = [
    (3, 7),
    (3, 2),
    (7, 3),
    (3, 3)
]
for test_tuple in data:
    print(uniquePaths(*test_tuple))
