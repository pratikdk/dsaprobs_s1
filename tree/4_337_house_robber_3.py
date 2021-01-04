from tree_node import TreeNode

def rob(root):
    res = [0, 0]
    def do_it(node, lvl):
        if node == None: return
        if lvl%2 == 0:
            res[0] += node.value
        else:
            res[1] += node.value
        do_it(node.left, lvl+1)
        do_it(node.right, lvl+1)
    do_it(root, 0)
    return max(res)


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
