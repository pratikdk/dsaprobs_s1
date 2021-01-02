from tree_node import TreeNode

def flatten(root):
    if root==None: return # End when hits bottom
    if root.left:
        left_rightmost = get_rightmost(root.left)
        left_rightmost.right = root.right
        root.right = root.left
        root.left = None
    flatten(root.right)

# def get_rightmost(node):
#     if node.right:
#         return get_rightmost(node.right)
#     else:
#         return node

def get_rightmost(node):
    if node == None: return None
    ret = get_rightmost(node.right)
    if ret == None: return node
    else: return ret


def printright(node):
    if node == None: return
    print(node.value)
    printright(node.right)


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left = n2
    n1.right = n4
    n4.left = n3
    n4.right = n5
    n5.right = n6
    #n5 = None
    #print(get_rightmost(n1).value)
    flatten(n1)
    printright(n1)
