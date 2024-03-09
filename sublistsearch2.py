#Remove all occurrences of second linked list from first linked list

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

def removeSublist(list1, sublist):
    if not list1 or not sublist:
        return list1

    dummy = Node(0)
    dummy.next = list1
    current = dummy

    while current.next:
        if current.next.value == sublist.value:
            temp1 = current.next
            temp2 = sublist
            while temp1.next and temp2.next and temp1.next.value == temp2.next.value:
                temp1 = temp1.next
                temp2 = temp2.next
            if not temp2.next:
                current.next = temp1.next
            else:
                current = current.next
        else:
            current = current.next

    return dummy.next
list1 = Node(1)
list1.next = Node(2)
list1.next.next = Node(3)
list1.next.next.next = Node(4)
list1.next.next.next.next = Node(2)
list1.next.next.next.next.next = Node(3)
list1.next.next.next.next.next.next = Node(5)
list1.next.next.next.next.next.next.next = Node(2)
list1.next.next.next.next.next.next.next.next = Node(3)

sublist = Node(2)
sublist.next = Node(3)

result = removeSublist(list1, sublist)
while result:
    print(result.value, end="->")
    result = result.next
