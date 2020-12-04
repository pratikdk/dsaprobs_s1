from linked_list import ListNode, nodelist_builder, printNodes

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def isPalindrome(node):
    slow = node
    fast = node
    stack = []
    while fast != None and fast.next != None:
        stack.append(slow.val)
        slow = slow.next
        fast = fast.next.next
    if fast != None:
         slow = slow.next
    while slow != None:
        if stack.pop() != slow.val:
            return False
        slow = slow.next
    return True

if __name__ == "__main__":
    #data = [1, 2, 3, 4, 4, 5]
    data = [
        [1, 1, 2, 3, 3, 2, 1, 1],
        [1, 2],
        [1, 2, 2, 1]
    ]
    for test_list in data:
        head = nodelist_builder(test_list)
        #printNodes(head)
        print(isPalindrome(head))
