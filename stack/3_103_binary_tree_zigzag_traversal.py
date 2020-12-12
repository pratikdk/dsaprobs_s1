class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    zzlist = []
    traverse(root, zzlist, 0)
    return zzlist

def traverse(node, zzlist, level):
    if node == None: return
    if len(zzlist) <= level:
        zzlist.append([])
    level_list = zzlist[level]
    if level%2 == 0: level_list.append(node.val)
    else: level_list.insert(0, node.val)
    traverse(node.left, zzlist, level+1)
    traverse(node.right, zzlist, level+1)


if __name__ == "__main__":
    n1 = TreeNode(3)
    n1.left = TreeNode(9)
    n1.right = TreeNode(20)
    n1.right.left = TreeNode(15)
    n1.right.right = TreeNode(7)
    print(zigzagLevelOrder(n1))
