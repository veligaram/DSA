#program for Nth node from the end of a linked list

class Node:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def push(self,new_data):
        new_node=Node(new_data)
        new_node.next=self.head
        self.head=new_node
    def printNth(self,n):
        temp=self.head
        length=0
        while temp is not None:
            temp=temp.next
            length+=1
        if n>length:
            print("location grater than the length of linked list")
            return
        temp=self.head
        for i in range(0,length-n):
            temp=temp.next
        print(temp.data)
if __name__=="__main__":
    li=LinkedList()
    li.push(20)
    li.push(4)
    li.push(15)
    li.push(35)
    li.printNth(4)
