from tree_node import TreeNode

# Inorder traversal
def kthSmallest(root, k):
    stack = []
    while True:
        while root != None:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if k == 0:
            return root.value
        root = root.right

if __name__ == "__main__":
    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(5)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    # [1, 2, 2, 4, 5] # inorder
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print(kthSmallest(n1, 2)) # not zero indexed
