from linked_list import ListNode, nodelist_builder, printNodes

next_sublist = None
tail = None

def printme():
    print(tail)

def sortList(head):
    if head == None or head.next == None:
        return head
    dummy_node = ListNode()
    next_sublist = ListNode()
    tail = ListNode()
    printme()
    print(tail)
    out_ptr = head
    size = 1
    while out_ptr.next != None:
        tail = dummy_node
        in_ptr = head
        while in_ptr != None:
            if in_ptr.next == None:
                tail.next = in_ptr
                break
            mid = split(in_ptr, size)
            merge(in_ptr, mid)
            in_ptr = next_sublist
        in_ptr = dummy_node.next
        #print(i)
        size += 1
        out_ptr = out_ptr.next


def get_length(head):
    counter = 0
    while head != None:
        counter += 1
        head = head.next
    return counter

def split(start, size):
    mid_prev = start
    end = start.next
    i = 1
    while i < size and (mid_prev.next != None or end.next != None):
        if end.next != None:
            end = end.next.next if end.next.next != None else end.next
        if mid_prev.next != None:
            mid_prev = mid_prev.next
    mid = mid_prev.next
    mid_prev.next = None
    next_sublist = end.next
    end.next = None
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
    while dummy_head.next != None:
        dummy_head = dummy_head.next
    tail.next = dummy_node.next
    tail = dummy_head


if __name__ == "__main__":
    data = [
        [5, 4, 3, 2, 1, -1],
        [2, 1],
        [1]
    ]
    for test_list in data:
        head = nodelist_builder(test_list)
        rhead = sortList(head)
        #printNodes(rhead)
        print("---x---")
