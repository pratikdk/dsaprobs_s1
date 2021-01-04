from tree_node import TreeNode

def rob(root):
    rob_saved = {}
    not_rob_saved = {}
    def helper(node, parent_robbed): # post order
        # Base case
        if node == None: return 0

        if parent_robbed: # Skipper, children adder
            if node in rob_saved:
                return rob_saved[node]
            result = helper(node.left, False) + helper(node.right, False)
            rob_saved[node] = result
            return result
        else: # parent adder
            if node in not_rob_saved:
                return not_rob_saved[node]
            rob = node.value + helper(node.left, True) + helper(node.right, True)
            not_rob = helper(node.left, False) + helper(node.right, False)
            result = max(rob, not_rob)
            not_rob_saved[node] = result
            return result

    return helper(root, False)

if __name__ == "__main__":
    # n1 = TreeNode(3)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # n4 = TreeNode(3)
    # n5 = TreeNode(1)
    # n1.left = n2
    # n1.right = n3
    # n2.right = n4
    # n3.right = n5
    # print(rob(n1))

    n1 = TreeNode(3)
    n2 = TreeNode(4)
    n3 = TreeNode(5)
    n4 = TreeNode(1)
    n5 = TreeNode(3)
    n6 = TreeNode(1)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6
    print(rob(n1))
