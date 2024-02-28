#convert singly linked list into circular linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
 
def convertToCircular(head):
    current = head
    while current.next != None:
        current = current.next
    current.next = head
 
 
 
def printList(head):
    current = head
    while True:
        print(current.data, end=" ")
        current = current.next
        if current == head:
            break
 
if __name__ == "__main__":
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    convertToCircular(head)
    print("The circular linked list is:")
    printList(head)
