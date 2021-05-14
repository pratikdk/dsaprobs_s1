from tree_node import TreeNode

def preorder(root):
    return [root.value] + preorder(root.left) + preorder(root.right) if root else []

def mergeTrees(t1, t2):
    # Base cases
    if not t1:
        return t2
    if not t2:
        return t1
    t1.value += t2.value # if both exist add both values and store in t1
    t1.left = mergeTrees(t1.left, t2.left) # attach t2.left to t1.left if t1.left is missing
    t1.right = mergeTrees(t1.right, t2.right)  # attach t2.right to t1.right if t1.right is missing
    return t1


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n1.left = n2
    n1.right = n3
    merged_tree = mergeTrees(n1, n4)
    print(preorder(merged_tree))
