# check if a singly linked list is palindrome

class Node:
    def __init__(self,data):
        self.data=data
        self.ptr=None

def ispalindrome(head):
    slow=head
    stack=[]
    ispalin=True
    while slow !=None:
        stack.append(slow.data)
        slow=slow.ptr

    while head !=None:
        i=stack.pop()
        if head.data==i:
            ispalin=True
        else:
            ispalin=False
            break

        head=head.ptr
    return ispalin

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(3)
six = Node(2)
seven = Node(1)
 
# Initialize the next pointer
# of every current pointer
one.ptr = two
two.ptr = three
three.ptr = four
four.ptr = five
five.ptr = six
six.ptr = seven
seven.ptr = None
 
# Call function to check palindrome or not
result = ispalindrome(one)
print(result)
