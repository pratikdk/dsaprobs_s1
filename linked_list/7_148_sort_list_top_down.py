from linked_list import ListNode, nodelist_builder, printNodes

def sortList(head):
    # Recursive split and merge
    if head == None or head.next == None:
        return head
    mid = get_mid_and_detach(head)
    left = sortList(head)
    right = sortList(mid)
    return merge(left, right)

def get_mid_and_detach(head):
    mid_prev = None
    if head != None and head.next != None:
        mid_prev = head if mid_prev == None else mid_prev.next
        head = head.next.next
    mid = mid_prev.next
    mid_prev.next = None
    return mid

def merge(left, right):
    dummy_node = ListNode()
    dummy_head = dummy_node
    while left != None and right != None:
        if left.val < right.val:
            dummy_head.next = left
            dummy_head = dummy_head.next
            left = left.next
        else:
            dummy_head.next = right
            dummy_head = dummy_head.next
            right = right.next
    dummy_head.next = left if left != None else right
    return dummy_node.next


if __name__ == "__main__":
    data = [
        [5, 4, 3, 2, 1, -1],
        [2, 1],
        [1]
    ]
    for test_list in data:

        head = nodelist_builder(test_list)
        rhead = sortList(head)
        printNodes(rhead)
        print("---x---")
