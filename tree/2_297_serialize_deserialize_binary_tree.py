from tree_node import TreeNode


def serialize(root):
    res = []
    queue = []
    queue.append(root)
    while len(queue) > 0:
        # pop
        node = queue.pop(0)
        if node == None and len(queue)>0:
            res.append(None)
        elif node:
            res.append(node.value)
        if node:
            queue.append(node.left)
            queue.append(node.right)
    return res



def deserialize(vals):
    #vals = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    #vals  = [1, 2, 3]
    buffer = []
    t_root = TreeNode(vals[0])
    buffer.append(t_root)
    val_head = 1
    while buffer:# and val_head < len(vals):
        next_buffer = []
        for n in buffer:
            if val_head < len(vals):
                #print(n.value, val_head)
                # Create
                n_l = TreeNode(vals[val_head]) if vals[val_head] else None
                val_head += 1
                n_r = TreeNode(vals[val_head]) if vals[val_head] else None
                val_head += 1
                # Connect
                n.left = n_l
                n.right = n_r
                # pop and push
                if n_l: next_buffer.append(n_l)
                if n_r: next_buffer.append(n_r)
        buffer = next_buffer
    return t_root
    # cons_array = []
    # inorder_print(t_root, cons_array)
    # print(cons_array)

if __name__ == "__main__":
    # n1 = TreeNode(1)
    # n2 = TreeNode(2)
    # n3 = TreeNode(3)
    # n4 = TreeNode(4)
    # n1.left = n2
    # n1.right = n4
    # n2.left = n3
    v1 = [1, 2, 4, 3, None, None, None, None, None]
    v2 = [10, 5, -3, 3, 2, None, 11, 3, -2, None, 1]
    t1 = deserialize(v1)
    t2 = deserialize(v2)
    print(serialize(t1))
    print(serialize(t2))
