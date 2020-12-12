class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def zigzagLevelOrder(root):
    res = []
    temp = []
    level = [root]
    next_level = []
    level_num = 0
    while level:
        for _ in range(len(level)):
            node = level.pop()
            if level_num%2 == 0: temp.append(node.val)
            else: temp.insert(0, node.val)
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
        res.append(temp)
        temp = []
        while next_level:
            level.append(next_level.pop())
        level_num += 1
    return res


if __name__ == "__main__":
    n1 = TreeNode(3)
    n1.left = TreeNode(9)
    n1.right = TreeNode(20)
    n1.right.left = TreeNode(15)
    n1.right.right = TreeNode(7)
    print(zigzagLevelOrder(n1))
