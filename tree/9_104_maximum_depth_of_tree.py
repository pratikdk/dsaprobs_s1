from tree_node import TreeNode

def maxDepth(root):
    if root == None: return 0
    left = maxDepth(root.left)
    right = maxDepth(root.right)
    return max(left, right) + 1

if __name__ == "__main__":
    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(7)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n6 = TreeNode(6)
    n7 = TreeNode(9)
    n8 = TreeNode(8)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    n7.right = n8
    print(maxDepth(None))
