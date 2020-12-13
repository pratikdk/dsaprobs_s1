class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    helper(root, res)
    return res

def helper(root, res):
    if root != None:
        if root.left != None:
            helper(root.left, res)
        res.append(root.val)
        if root.right != None:
            helper(root.right, res)

if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    print(inorderTraversal(t1))
