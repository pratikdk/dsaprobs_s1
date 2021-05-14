from tree_node import TreeNode
# Inorder Traversal
def kthSmallest(root, k):
    def inorder(r):
        return (inorder(r.left) + [r.value] + inorder(r.right)) if r else []
    return inorder(root)[k-1]

if __name__ == "__main__":
    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(5)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    print(kthSmallest(n1, 2)) # not zero indexed
