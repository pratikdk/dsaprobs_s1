from linked_list import ListNode, nodelist_builder, printNodes


# def delete(node):
#     print("Node here is:", node.val)
#     if node != None and node.next != None:
#         node.val = node.next.val
#         node.next = node.next.next

def delete(node, val):
    dummy_node = ListNode(None)
    prev = dummy_node
    prev.next = node
    while node != None:
        #print(node.val)
        #print(prev.val, end = " ")
        next = node.next
        if node.val == val:
            #print("yes")
            prev.next = next
        else:
            prev = node
        #print(prev.val)
        node = next
    return dummy_node.next

if __name__ == "__main__":
    data = [
        ([4, 5, 1, 9], 5),
        ([4, 5, 1, 9], 1),
        ([1, 2, 3, 4], 3),
        ([0, 1], 0),
        ([1], 1),
        ([-3, 5, -99], -3)
    ]
    for test_list in data:
        head = nodelist_builder(test_list[0])
        # dnode = head
        # while dnode != None:
        #     if dnode.val == test_list[1]:
        #         break
        #     dnode = dnode.next
        # delete(dnode)
        new_node = delete(head, test_list[1])
        printNodes(new_node)
        print("---x---")
