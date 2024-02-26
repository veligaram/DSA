#remove duplicates from a sorted doubly linked list

class Node:
    def __init__(self,new_data):
        self.data=new_data
        self.next=None
        self.prev=None
def deletingNode(head_ref,_del):
    if (head_ref==None or _del==None):
        return
    if (head_ref==_del):
        head_ref=_del.next
    if (_del.next !=None):
        _del.next.prev=_del.prev
    if (_del.prev !=None):
        _del.prev.next=_del.next
    return head_ref
def removeDuplicates(head_ref):
    if ((head_ref)==None):
        return None
    current=head_ref
    next=None
    while(current.next !=None):
        if (current.data==current.next.data):
            deletingNode(head_ref,current.next)
        else:
            current=current.next
    return head_ref
def push(head_ref,new_data):
    new_node=Node(0)
    new_node.data=new_data
    new_node.prev=None
    new_node.next=(head_ref)
    if ((head_ref) !=None):
        (head_ref).prev=new_node
    (head_ref)=new_node
    return head_ref
def printList(head):
    if head==None:
        print("empty doubly linked list")
    while(head !=None):
        print(head.data,end=" ")
        head=head.next
head=None
head = push(head, 12)
head = push(head, 12)
head = push(head, 10)
head = push(head, 8)
head = push(head, 8)
head = push(head, 6)
head = push(head, 4)
head = push(head, 4)
head = push(head, 4)
head = push(head, 4)
head = removeDuplicates(head)
printList(head)
