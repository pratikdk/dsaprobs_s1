class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    res = []
    curr = root
    pre = None
    while curr != None:
        if curr.left == None:
            res.append(curr.val)
            curr = curr.right
        else:
            pre = curr.left
            while pre.right != None:
                pre = pre.right
            pre.right = curr
            temp = curr
            curr = curr.left
            temp.left = None
    return res

if __name__ == "__main__":
    t1 = TreeNode(1)
    t2 = TreeNode(2)
    t3 = TreeNode(3)
    t4 = TreeNode(4)
    t1.left = t2
    t1.right = t3
    t3.left = t4
    print(inorderTraversal(t1))
