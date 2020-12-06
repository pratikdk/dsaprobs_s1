from linked_list import ListNode, nodelist_builder, printNodes

class Info:
    def __init__(self, size=0, tail=None):
        self.size = size
        self.tail = tail

def get_info(node):
    counter = 1
    while node.next != None:
        counter += 1
        node = node.next
    return Info(counter, node)

def get_kth_node(node, k):
    while k>0 and node != None:
        node = node.next
        k -= 1
    return node

def getIntersectionNode(headA, headB):
    ainfo = get_info(headA)
    binfo = get_info(headB)
    if ainfo.tail != binfo.tail:
        return None
    shorter = headA if ainfo.size < binfo.size else headB
    longer = headB if ainfo.size < binfo.size else headA
    # Shift head of longer list to match with shorter length
    longer = get_kth_node(longer, abs(ainfo.size - binfo.size))
    while shorter != longer:
        shorter = shorter.next
        longer = longer.next
    return longer

if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)
    # list 1
    n1.next = n2
    n2.next = n3
    n3.next = n5
    # List 2
    n4.next = n3
    n3.next = n5

    printNodes(n1)
    print()
    printNodes(n4)
    print("Intersection at:", getIntersectionNode(n1, n4).val)
    #print("Intersection:", find_intersection(n1, n4).data)
