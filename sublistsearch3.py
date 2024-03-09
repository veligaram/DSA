#concatenate the sublists

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def concatenateSublists(list1, list2):
    if not list1:
        return list2
    if not list2:
        return list1

    current = list1
    while current.next:
        current = current.next

    current.next = list2
    return list1
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)

list2 = Node(4)
list2.next = Node(5)
list2.next.next = Node(6)

result = concatenateSublists(list1, list2)
while result:
    print(result.value, end="->")
    result = result.next
