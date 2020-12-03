class ListNode():
    def __init__(self, data=0, next=None):
        self.val = data
        self.next = None

class LinkedList():
    def __init__(self):
        self.head = self.tail = None

    def printList(self):
        temp = self.head
        while(temp):
            print(temp.val)
            temp = temp.next

def linkedList_builder(data):
    llist = LinkedList()
    previous = None
    for i in data:
        if llist.head:
            previous.next = ListNode(i)
            previous = previous.next
        else:
            llist.head = ListNode(i)
            previous = llist.head
    return llist

def nodelist_builder(data):
    head = None
    tail = None
    for i in data:
        if head:
            tail.next = ListNode(i)
            tail = tail.next
        else:
            head = tail = ListNode(i)
    return head

def printNodes(head):
    while(head):
        print(head.val)
        head = head.next

if __name__ == "__main__":
    llist = LinkedList()
    first = ListNode(1)
    second = ListNode(2)
    third = ListNode(3)
    llist.head = first
    first.next = second
    second.next = third

    llist.printList()
