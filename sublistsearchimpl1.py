#implementation of sublist search using iteration

class Node:
    def __init__(self,value=0):
        self.value=value
        self.next=None
def findlist(llist1,llist2):
    if not llist1 and not llist2:
        return True
    if not llist1 or llist2:
        return False
    prt1=llist1
    ptr2=llist2
    while ptr2:
        ptr2=llist2
        while ptr1:
            if not ptr2:
                return False
            elif ptr1.value==ptr2.value:
                ptr1=ptr1.next
                ptr2=ptr2.next
            else:
                break
        if not ptr1:
            return True
        ptr1=llist1
        llist2=llist2.next
    return False
node_a = Node(1)
node_a.next = Node(2)
node_a.next.next = Node(3)
node_a.next.next.next = Node(4)
 
node_b = Node(1)
node_b.next = Node(2)
node_b.next.next = Node(1)
node_b.next.next.next = Node(2)
node_b.next.next.next.next = Node(3)
node_b.next.next.next.next.next = Node(4)
 
if findlist(node_a, node_b):
    print("LIST FOUND")
else:
    print("LIST NOT FOUND")
    
