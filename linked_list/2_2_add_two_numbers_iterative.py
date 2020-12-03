# (7-> 1 -> 6) + (5 -> 9 -> 2).That is,617 + 295 = 912
from linked_list import ListNode, nodelist_builder, printNodes

def addTwoNumbers(l1, l2):
    dummy_node = ListNode(0)
    p1 = l1
    p2 = l2
    carry = 0
    curr = dummy_node
    while p1 != None or p2 != None:
        x = p1.val if p1 != None else 0
        y = p2.val if p2 != None else 0
        sum = carry + x + y
        carry = sum//10
        curr.next = ListNode(sum%10)
        curr = curr.next
        if p1 != None: p1 = p1.next
        if p2 != None: p2 = p2.next
    return dummy_node.next


if __name__ == "__main__":
    data = [
        ([7, 1, 6], [5, 9, 2])
        #([9, 9], [9, 9])
    ]
    head1 = nodelist_builder(data[0][0])
    head2 = nodelist_builder(data[0][1])
    rhead = addTwoNumbers(head1, head2)
    #delete_middle_node(head.next.next)
    printNodes(rhead)
