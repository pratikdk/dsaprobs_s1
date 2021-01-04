from tree_node import TreeNode

def rob(root):
    if root == None: return 0
    tree = []
    graph = {-1:[]}
    index = -1
    queue = [(root, -1)]
    while queue:
        node, parent_index = queue.pop(0)
        if node:
            index += 1
            tree.append(node.value)
            graph[index] = []
            graph[parent_index].append(index)
            queue.append((node.left, index))
            queue.append((node.right, index))
    # Initialize dp arrays
    dp_rob = [0] * (index+1)
    dp_not_rob = [0] * (index+1)
    # Reverse process
    for i in reversed(range(index+1)):
        # if node is leaf
        if not graph[i]:
            dp_rob[i] = tree[i]
            dp_not_rob[i] = 0
        else:
            # Sum using this node
            dp_rob[i] = tree[i] + sum(dp_not_rob[child] for child in graph[i])
            # Sum using children or not
            dp_not_rob[i] = sum(max(dp_rob[child], dp_not_rob[child]) for child in graph[i])
    return max(dp_rob[0], dp_not_rob[0])


if __name__ == "__main__":
    # n1 = TreeNode(3)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # n4 = TreeNode(3)
    # n5 = TreeNode(1)
    # n1.left = n2
    # n1.right = n3
    # n2.right = n4
    # n3.right = n5
    # print(rob(n1))

    n1 = TreeNode(3)
    n2 = TreeNode(4)
    n3 = TreeNode(5)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n6 = TreeNode(1)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    print(rob(n1))
