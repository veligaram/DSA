#rotate doubly linked list by N nodes

class Node:
    def __init__(self,data):
        self.data=data
        self.pre=None
        self.next=None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insertAtHead(self,data):
        n=Node(data)
        if self.head==None:
            self.head=n
            return
        n.next=self.head
        self.head.pre=n
        self.head=n
        return
    def insertAtTail(self,data):
        if self.head==None:
            self.insertAtHead(data)
            return
        temp=self.head
        while temp.next !=None:
            temp=temp.next
        n=Node(data)
        temp.next=n
        n.pre=temp
        return
    def display(self):
        temp=self.head
        while temp !=None:
            print(temp.data,"-->",sep="",end="")
            temp=temp.next
        print("NULL")
    def rotateByN(self,pos):
        if pos==0:
            return
        curr=self.head
        while pos:
            curr=curr.next
            pos-=1
        tail=curr.pre
        NewHead=curr
        tail.next=None
        curr.pre=None
        while curr.next !=None:
            curr=curr.next
        curr.next=self.head
        self.head.pre=curr
        self.head=NewHead
if __name__=="__main__":
    li=DoublyLinkedList()
    li.insertAtTail('a')
    li.insertAtTail('b') 
    li.insertAtTail('c') 
    li.insertAtTail('d') 
    li.insertAtTail('e') 
  
    n = 2
    print("Before Rotation : ") 
    li.display() 
    li.rotateByN(n) 
    print("\nAfter Rotation : ") 
    li.display() 
    print() 
