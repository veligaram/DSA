#delete middle element of stack

def delete_middle(stack,n,current=0):
    if not stack or current ==n:
        return
    temp=stack.pop()
    delete_middle(stack,n,current+1)
    if current !=n//2:
        stack.append(temp)
stack=[1,2,3,4,5]
n=len(stack)
print("before deleting:",stack)
delete_middle(stack,n)
print("stack after deleting middle value:",stack)
