#count the number of occurrences of a sublist
class Node:
    def __init__(self,value):
        self.value=value
        self.next=None
        
def countSublists(list1, sublist):
    if not list1 or not sublist:
        return 0
    count = 0
    current1 = list1
    current2 = sublist
    while current1:
        if current1.value == current2.value:
            temp1 = current1
            temp2 = current2
            while temp1 and temp2 and temp1.value == temp2.value:
                temp1 = temp1.next
                temp2 = temp2.next
            if not temp2:
                count += 1
        current1 = current1.next
    return count
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

print(countSublists(list1, sublist))
