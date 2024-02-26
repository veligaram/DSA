#doubly linked list

#creation of node in doubly linked list

class Node:
    def __init__(self,next=None,prev=None,data=None):
        self.next=next
        self.prev=prev
        self.data=data
class DoublyLinkedList:
    def __init__(self):
        self.head=None
    def insert_at_beggining(self,new_data):
        new_node=Node(data=new_data)
        new_node.next=self.head
        new_node.prev=None
        if self.head is not None:
            self.head.prev=new_node
        self.head=new_node
#inserting a node after a given node in a doubly linked list
    def insert_after(self,prev_node,new_data):
        if prev_node is None:
            print("node doesn't exist in Doubly linked list")
            return
        new_node=Node(data=new_data)
        new_node.next=prev_node.next
        prev_node.next=new_node
        new_node.prev=prev_node
        if new_node.next is not None:
            new_node.next.prev=new_node
#inserting a node before a given node
    def insert_before(self,next_node,new_data):
        if next_node is None:
            print("node doesn't exist in Doubly linked list")
            return
        new_node=Node(data=new_dta)
        new_node.prev=next_node.prev
        next_node.prev=new_node
        if new_node.prev is not None:
            new_node.prev.next=new_node
        else:
            head=new_node
#inserting at the end of the doubly linked list
    def insert_at_end(self,new_data):
        new_node=Node(data=new_data)
        last=self.head
        new_node.next=None
        if self.head is None:
            new_node.prev=None
            self.head=new_node
            return
        while(last.next is not None):
            last=last.next
        last.next=new_node
        new_node.prev=last
#printing the doubly likedlist
    def printList(self, node):
        while(node is not None):
            print(node.data, end=' ')
            node = node.next
if __name__=="__main__":
    dll=DoublyLinkedList()
    dll.insert_at_beggining(2)
    dll.insert_at_end(4)
    dll.insert_at_beggining(8)
    dll.insert_after(2,10)
    dll.insert_before(2,15)
    dll.printList()
        
