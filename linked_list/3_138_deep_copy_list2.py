# [[7,null],[13,0],[11,4],[10,2],[1,0]]

def copyRandomList(node):
    if node == None: return None
    head = node
    while head != None:
        next = head.next
        new_node = Node(head.val)
        head.next = new_node
        new_node.next = next
        head = next
    head = node
    while head != None:
        if head.random != None:
            head.next.random = head.random.next
        head = head.next.next
    head = node
    dummy_node = Node(0)
    copy = None
    dummy_head = dummy_node
    while head != None:
        next = head.next.next
        copy = head.next
        dummy_head.next = copy
        dummy_head = copy
        head.next = next
        head = next
    dummy_node.next


class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random

def printNodes(node):
    while node != None:
        print(node.val, "->", node.next.val if node.next else None, "random:", node.random.val if node.random else None)
        node = node.next

if __name__ == "__main__":
    data = [
        [[7,None],[13,0],[11,4],[10,2],[1,0]],
        [[1,1],[2,1]],
        [[3,None],[3,0],[3,None]],
        []
    ]
    for i, test_list in enumerate(data):
        print("Index:", i)
        nodes = []
        for node in test_list:
            nodes.append(Node(node[0]))
        for j, node in enumerate(test_list):
            if j < len(nodes)-1:
                nodes[j].next = nodes[j+1]
            else:
                nodes[j].next = None
            nodes[j].random = nodes[node[1]] if node[1] != None else None
        #rhead = copyRandomList(nodes[0])
        if len(nodes)>0:
            rhead = copyRandomList(nodes[0])
            printNodes(nodes[0])
            print()
            printNodes(rhead)
        else:
            rhead = copyRandomList(None)
            print()
        print("--------")
