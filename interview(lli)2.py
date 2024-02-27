#reverse a sublist of linked list
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverseBetween(head, m, n):
    if not head or m == n:
        return head

    dummy = ListNode(0)
    dummy.next = head
    pre = dummy
    for _ in range(m - 1):
        pre = pre.next

    current = pre.next
    prev = None

    for _ in range(n - m + 1):
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    pre.next.next = current
    pre.next = prev

    return dummy.next

def printLinkedList(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")


head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
print("Original Linked List:")
printLinkedList(head)

m, n = 2, 4
head = reverseBetween(head, m, n)

print("\nLinked List after reversing from position {} to {}:".format(m, n))
printLinkedList(head)
