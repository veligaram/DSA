#reverse a linked list in groups of given size
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def reverse(self,head,k):
        if head== None:
            return None
        current=head
        next=None
        prev=None
        count=0
        while(current is not None and count <k):
            next=current.next
            current.next=prev
            prev=current
            current=next
            count +=1
        if next is not None:
            head.next=self.reverse(next,k)
        return prev
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        temp=self.head
        while(temp):
            print(temp.data,end=" ")
            temp=temp.next
li=LinkedList()
li.push(9)
li.push(8) 
li.push(7) 
li.push(6) 
li.push(5) 
li.push(4) 
li.push(3) 
li.push(2) 
li.push(1) 
  
print("Given linked list") 
li.printList() 
li.head = li.reverse(li.head, 3) 
  
print ("\nReversed Linked list") 
li.printList() 
