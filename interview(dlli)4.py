#sort a K sorted doubly linked list

head = None
 
class Node:
    def __init__(self, val):
        self.data = val
        self.prev = None
        self.next = None

def sortAKSortedDLL(head , k):
    if (head == None or head.next == None):
        return head
    i = head.next
    while(i != None):
        j = i
         
        while (j.prev != None and j.data < j.prev.data):
           
            temp = j.prev.prev
            temp2 = j.prev
            temp3 = j.next
            j.prev.next = temp3
            j.prev.prev = j
            j.prev = temp
            j.next = temp2
            if (temp != None):
                temp.next = j
            if (temp3 != None):
                temp3.prev = temp2
                 
        if (j.prev == None):
            head = j
        i = i.next
 
    return head
 
def push(new_data):
 
    global head
    new_node = Node(new_data)
    new_node.prev = None
    new_node.next = head
 
    if (head != None):
        head.prev = new_node
 
    
    head = new_node
def printList(node):
    while (node != None):
        print(node.data,end = " ")
        node = node.next
push(8)
push(56)
push(12)
push(2)
push(6)
push(3)
 
k = 2
 
print("Original Doubly linked list:")
printList(head)
 
sortedDLL = sortAKSortedDLL(head, k)
print("")
print("Doubly Linked List after sorting:")
printList(sortedDLL)
