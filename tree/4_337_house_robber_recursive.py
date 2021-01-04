from tree_node import TreeNode

def rob(root):
    def helper(node): # post order
        # Base case
        if node == None: return (0, 0)
        # left and right
        left = helper(node.left)
        right = helper(node.right)
        # Rob this node and skip children
        rob = node.value + left[1] + right[1]
        # Don't rob this, but rob children or don't
        not_rob = max(left) + max(right)
        # return rob and not_rob for this node
        return [rob, not_rob]

    return max(helper(root))

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
