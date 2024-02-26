#find the largest node in doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def findLargestNode(head):
    if not head:
        return None

    largest_node = head

    current = head.next
    while current:
        if current.data > largest_node.data:
            largest_node = current
        current = current.next

    return largest_node

head = Node(4)
head.next = Node(7)
head.next.prev = head
head.next.next = Node(2)
head.next.next.prev = head.next
head.next.next.next = Node(9)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(5)
head.next.next.next.next.prev = head.next.next.next

largest_node = findLargestNode(head)

if largest_node:
    print("The largest node in the doubly-linked list is:", largest_node.data)
else:
    print("The doubly-linked list is empty.")
