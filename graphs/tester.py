class Node:
	def __init__(self, val, next=None):
		self.value = val
		self.next = next

def reverse_linked_list(node):
    next = node.next
    node.next = None
    while next:
        tmp = next.next
        next.next = node
        node = next
        next = tmp

def reverse_linked_list2(node): # current
    previous = None
    while node:
        next = node.next
        node.next = previous
        previous = node
        node = next

def print_llist(node):
	while node:
		print(node.value, end=" ")
		node = node.next
	print("\n")


n0 = Node(0)
n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
print_llist(n0)
reverse_linked_list2(n0)
print_llist(n4)
