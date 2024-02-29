#remove duplicates from an unsorted doubli linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node
            new_node.prev = temp

    def remove_duplicates(self):
        if not self.head:
            return

        seen_data = set()
        current = self.head

        while current:
            if current.data not in seen_data:
                seen_data.add(current.data)
                current = current.next
            else:
                next_node = current.next
                if next_node:
                    next_node.prev = current.prev
                current.prev.next = next_node
                del current
                current = next_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()

if __name__ == "__main__":
    dlist = DoublyLinkedList()
    for data in [1, 2, 3, 2, 4, 5, 4, 6, 7]:
        dlist.append(data)

    print("Original Doubly Linked List:")
    dlist.print_list()

    dlist.remove_duplicates()

    print("\nDoubly Linked List after removing duplicates:")
    dlist.print_list()
