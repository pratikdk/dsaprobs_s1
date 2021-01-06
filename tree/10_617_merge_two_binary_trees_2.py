from tree_node import TreeNode

def preorder(root):
    return [root.value] + preorder(root.left) + preorder(root.right) if root else []

# Iterative approach
def mergeTrees(t1, t2):
    if t1 == None:
        return t2

    stack = []
    stack.append((t1, t2))
    while stack:
        t = stack.pop()
        # If any of the tree node is None, skip this iteration to pop next
        if t[0] == None or t[1] == None:
            continue
        # Both nodes are present, add them to first
        t[0].value += t[1].value
        ## LEFT CHILD
        # offload children to the stack
        if t[0].left == None: # if t1's is child missing, attach t2's child
            t[0].left = t[1].left
        else: # Push childs, Dont bother about t2's child if missing, just NOne to stack
            stack.append((t[0].left, t[1].left))
        ## RIGHT CHILD
        # offload children to the stack
        if t[0].right == None: # if t1's is child missing, attach t2's child
            t[0].right = t[1].right
        else: # Push childs, Dont bother about t2's child if missing, just NOne to stack
            stack.append((t[0].right, t[1].right))
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
