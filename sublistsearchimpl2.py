#implementation of sublist search with recursion

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
 
def isSublist(list, sublist):
    if sublist is None:
        return True
    if list is None:
        return False
    if list.data == sublist.data:
        return isSublist(list.next, sublist.next)
    else:
        return isSublist(list.next, sublist)

list = Node(1)
list.next = Node(2)
list.next.next = Node(1)
list.next.next.next = Node(2)
list.next.next.next.next = Node(3)
list.next.next.next.next.next = Node(4)

sublist = Node(1)
sublist.next = Node(2)
sublist.next.next = Node(3)
sublist.next.next.next = Node(4)
if isSublist(list, sublist):
    print("LIST FOUND")
else:
    print("LIST NOT FOUND")
