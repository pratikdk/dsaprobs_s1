def numTrees(n):
    g = [0] * (n+1)
    g[0], g[1] = 1, 1
    for i in range(2, n+1):
        for j in range(1, i+1):
            g[i] += g[j-1] * g[i-j]
    return g[n] # num of bst at full capacity

if __name__ == "__main__":
    #for i in range(1, 5):
    print(numTrees(2))

# construct with each node as root
# consider this scenario
# if [1, 2, 3 , 4, 5]
# if 2 is root then g[2] 
