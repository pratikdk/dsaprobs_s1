from tree_node import TreeNode

class Codec:
    def serialize(self, root):
        res = []
        def do_it(node):
            if node:
                res.append(str(node.value))
                do_it(node.left)
                do_it(node.right)
            else:
                res.append('#')
        do_it(root)
        return " ".join(res)


    # def deserialize(self, data):
    #     def do_it():
    #         val = next(vals)
    #         if val == '#':
    #             return None
    #         node = TreeNode(int(val))
    #         node.left = do_it()
    #         node.right = do_it()
    #         return node
    #     vals = iter(data.split())
    #     return do_it()

    def deserialize(self, data):
        def doit():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()
            return node
        vals = iter(data.split())
        return doit()


if __name__ == "__main__":
    n1 = TreeNode(1)
    n2 = TreeNode(2)
    n3 = TreeNode(3)
    n4 = TreeNode(4)
    n5 = TreeNode(5)
    n6 = TreeNode(6)
    n1.left = n2
    n1.right = n3
    n2.left = n4
    n2.right = n5
    n3.right = n6

    c = Codec()

    s1 = c.serialize(n1)
    print("Serialized: " + s1)

    t1 = c.deserialize(s1)
