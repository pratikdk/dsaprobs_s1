from linked_list import ListNode, nodelist_builder, printNodes

def merge(l1, l2):
    if l1 == None and l2 == None: return None
    dummy_node = ListNode()
    dummy_head = dummy_node
    while l1 != None and l2 != None:
        if l1.val < l2.val:
            dummy_head.next = l1
            #dummy_head = dummy_head.next
            l1 = l1.next
        else:
            dummy_head.next = l2
            #dummy_head = dummy_head.next
            l2 = l2.next
        dummy_head = dummy_head.next
    dummy_head.next = l1 if l1 != None else l2
    return dummy_node.next


if __name__ == "__main__":
    data = [
        ([1,2,4], [1,3,4]),
        ([], []),
        ([], [0])
    ]
    for test_list in data:
        l1 = nodelist_builder(test_list[0])
        l2 = nodelist_builder(test_list[1])
        m_node = merge(l1, l2)
        printNodes(m_node)
        print("---x---")
