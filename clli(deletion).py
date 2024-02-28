#deletion operation in circular linkedlist

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.next = None
def push(head, data):  
    newP = Node(data) 
    newP.next = head  
    if head != None: 
        temp = head 
        while (temp.next != head): 
            temp = temp.next
        temp.next = newP 
    else: 
        newP.next = newP 
    head = newP 
    return head 
   
def printList(head): 
    if head == None: 
        print("List is Empty") 
        return
    temp = head.next
    print(head.data, end=' ') 
    if (head != None): 
        while (temp != head): 
            print(temp.data, end=" ") 
            temp = temp.next
    print() 

  
  
def deleteNode(head, key): 
    if (head == None): 
        return
 
    if (head.data == key and head.next == head): 
        head = None
        return
  
    last = head  
    if (head.data == key):  
        while (last.next != head): 
            last = last.next 
        last.next = head.next
        head = last.next
        return
    while (last.next != head and last.next.data != key): 
        last = last.next
    if (last.next.data == key): 
        d = last.next
        last.next = d.next
        d = None
    else: 
        print("Given node is not found in the list!!!") 
head = None
head = push(head, 2) 
head = push(head, 5) 
head = push(head, 7) 
head = push(head, 8) 
head = push(head, 10) 
  
print("List Before Deletion: ") 
printList(head) 
  
deleteNode(head, 7) 
print("List After Deletion: ") 
printList(head) 
