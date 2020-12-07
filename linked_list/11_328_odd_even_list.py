from linked_list import ListNode, nodelist_builder, printNodes

def oddEvenList(head):
    if head == None or head.next == None: return head
    f1 = head
    f2 = head.next
    start = f1
    mid = f2
    while head != None and head.next != None:
        head = head.next.next
        if head != None:
            f1.next = head
            f1 = f1.next
            f2.next = head.next
            f2 = f2.next
    f1.next = mid
    return start

if __name__ == "__main__":
    data = [
        [1, 2, 3, 4, 5],
        [60, 50, 40, 30, 20, 10],
        [],
        [3, 2],
        [1]
    ]
    for test_list in data:
        head = nodelist_builder(test_list)
        rhead = oddEvenList(head)
        printNodes(rhead)
        print("---x---")
