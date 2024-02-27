#add two numbers represented by linked list
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
        n=self.head
        while n:
            print(n.data,end=" ")
            n=n.next
        print()
def addTwoLists(first,second):
    num1,num2=0,0
    while first.head:
        num1=num1*10 + first.head.data
        first.head=first.head.next
    while second.head:
        num2=num2*10+ second.head.data
        second.head=second.head.next
    num3=num1+num2
    temp=LinkedList()
    while num3:
        last=num3%10
        temp.push(last)
        num3=num3//10
    return temp
if __name__=="__main__":
    first=LinkedList()
    second=LinkedList()
    first.push(6)
    first.push(4)
    first.push(9)
    first.push(5)
    first.push(7)
 
    second.push(4)
    second.push(8)
 
    ans = addTwoLists(first, second)
    ans.printList()
