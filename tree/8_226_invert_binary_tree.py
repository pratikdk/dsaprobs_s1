from tree_node import TreeNode

def invertTree(root):
    queue = []
    queue.append(root)
    while queue and root:
        node = queue.pop(0)
        node.left, node.right = node.right, node.left
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return root


def preorder(root):
    return [root.value] + preorder(root.left) + preorder(root.right) if root else []


if __name__ == "__main__":
    n1 = TreeNode(4)
    n2 = TreeNode(2)
    n3 = TreeNode(7)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n6 = TreeNode(6)
    n7 = TreeNode(9)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.left = n6
    n3.right = n7
    print(preorder(n1))
    print(preorder(invertTree(n1)))
    print(preorder(invertTree(None)))
