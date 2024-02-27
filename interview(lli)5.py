#multiply two numbers represented by linkedlists
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printList(self):
        ptr=self.head
        while(ptr !=None):
            print(ptr.data,end=" ")
            if ptr.next !=None:
                print("->",end=" ")
            ptr=ptr.next
        print()
def multiply(first,second):
    num1=0
    num2=0
    first_ptr=first.head
    second_ptr=second.head
    while first_ptr !=None or second_ptr !=None:
        if first_ptr !=None:
            num1=(num1*10) + first_ptr.data
            first_ptr=first_ptr.next
        if second_ptr !=None:
            num2=(num2*10) + second_ptr.data
            second_ptr=second_ptr.next
    return num1*num2
if __name__=="__main__":
    first=LinkedList()
    second=LinkedList()
    first.push(6) 
    first.push(4) 
    first.push(9)
    second.push(4) 
    second.push(8)
    print(multiply(first, second)) 
  
        
