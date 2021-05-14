from tree_node import TreeNode

class Solution(object):
    def diameterOfBinaryTree(self, root):
        self.ans = 0
        def depth(node):
            if not node: return 0
            L = depth(node.left)
            R = depth(node.right)
            self.ans = max(self.ans, L+R) # How much deep does each(l, r) side go, then do L + R
            return max(L, R) + 1

        depth(root)
        return self.ans


if __name__ == "__main__":
    s = Solution()
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left = n2
    n1.right = n4
    n2.left = n3
    n3.right = n5
    n4.right = n6
    #n5 = None
    print(s.diameterOfBinaryTree(n1))
