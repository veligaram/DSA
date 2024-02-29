#reverse a doubli linked list in groups of given size

class Node: 
    def __init__(self):
        self.data = 0; 
        self.next = None;
        self.next = None;
 
def insertAtEnd(head, data):
    new_Node = Node();
    new_Node.data = data;
    new_Node.next = None;
    temp = head;
 
    if (head == None):
        new_Node.prev = None;
        head = new_Node;
        return head;
     
 
    while (temp.next != None):
        temp = temp.next;
     
    temp.next = new_Node;
    new_Node.prev = temp;
    return head;
 
 
def printDLL(head):
    while (head != None):
        print(head.data, end=" ");
        head = head.next;
     
    print();
 
def reverseByN(head, k):
    if (head == None):
        return None;
 
    head.prev = None;
    temp=None;
    curr = head;
    newHead = None;
    count = 0;
 
    while (curr != None and count < k):
        newHead = curr;
        temp = curr.prev;
        curr.prev = curr.next;
        curr.next = temp;
        curr = curr.prev;
        count += 1;
     
    if (count >= k):
        rest = reverseByN(curr, k);
        head.next = rest;
        if (rest != None):
            rest.prev = head;
     
    return newHead;
if __name__ == '__main__':
    head = None;
    for i in range(1,11):
        head = insertAtEnd(head, i);
     
    printDLL(head);
    n = 4;
 
    head = reverseByN(head, n);
    printDLL(head);
