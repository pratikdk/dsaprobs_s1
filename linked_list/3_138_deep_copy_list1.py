# [[7,null],[13,0],[11,4],[10,2],[1,0]]

def copyRandomList(node):
    map = {}
    head = node
    while head != None:
        map[head] = Node(head.val)
        head = head.next
    map[None] = None
    head = node
    while head != None:
        map[head].next = map[head.next]
        map[head].random = map[head.random]
        head = head.next
    return map[node]

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
        rhead = copyRandomList(nodes[0])
        if len(nodes)>0:
            printNodes(nodes[0])
            print()
            printNodes(rhead)
        else:
            print()
        print("--------")
