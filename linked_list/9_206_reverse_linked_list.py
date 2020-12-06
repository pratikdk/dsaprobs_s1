from linked_list import ListNode, nodelist_builder, printNodes

def reverse(node):
    if node == None: return None
    dummy_node = ListNode()
    head = dummy_node
    while node != None:
        next = node.next
        node.next = head.next #None if head.next == None else
        head.next = node
        node = next
    return dummy_node.next

if __name__ == "__main__":
    data = [
        [1, 2, 3, 4, 5],
        [50, 40, 30, 20, 10],
        [],
        [3, 2]
    ]
    for test_list in data:
        head = nodelist_builder(test_list)
        rnode = reverse(head)
        printNodes(rnode)
        print("---x---")
