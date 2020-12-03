from linked_list import ListNode, nodelist_builder, printNodes

class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        for i in range(n):
            fast = fast.next
        while fast.next != None:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next


if __name__ == "__main__":
    sol = Solution()
    data = [
        ([1,2,3,4,5], 2),
        ([1], 1),
        ([1, 2], 1),
        ([1, 2], 2)
    ]
    for test_list in data:
        head = nodelist_builder(test_list[0])
        printNodes(head)
        print()
        rhead = sol.removeNthFromEnd(head, test_list[1])
        printNodes(rhead)
        print("----")
