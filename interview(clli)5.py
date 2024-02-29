#remove duplicate element from sorted linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def remove_duplicates_sorted_list(head):
    current = head

    while current and current.next:
        if current.data == current.next.data:
            current.next = current.next.next
        else:
            current = current.next

    return head

def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()

if __name__ == "__main__":
    head = Node(1)
    head.next = Node(1)
    head.next.next = Node(2)
    head.next.next.next = Node(2)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(4)

    print("Original Sorted Linked List:")
    print_list(head)

    head = remove_duplicates_sorted_list(head)

    print("\nSorted Linked List after removing duplicates:")
    print_list(head)
