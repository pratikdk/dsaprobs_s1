from tree_node import TreeNode

def levelOrder(root):
    if root == None: return None
    lvl_ord = []
    queue = []
    queue.append(root)
    while queue:
        buffer = []
        lvl_ord.append([])
        for node in queue:
            if node.left:
                buffer.append(node.left)
            if node.right:
                buffer.append(node.right)
            lvl_ord[-1].append(node.value)
        queue = buffer
    return lvl_ord

#
# def levelOrder(root):
#     if root == None: return None
#     lvl_ord = []
#     queue = []
#     queue.append(root)
#     while queue:
#         buffer = []
#         for node in queue:
#
#         node = queue.pop(0)
#         lvl_ord.append(node.val)
#         if node.left:
#             queue.append(node.left)
#         if node.right:
#             queue.append(node.right)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n1.left = n2
    n1.right = n3
    n3.left = n4
    n3.right = n5
    print(levelOrder(n1))
