#reverse a stack using queue

from queue import Queue

def reverse_stack(stack):
    if not stack:
        return
    queue1 = Queue()
    queue2 = Queue()
    while stack:
        queue1.put(stack.pop())
    while not queue1.empty():
        queue2.put(queue1.get())


    while not queue2.empty():
        stack.append(queue2.get())

stack_to_reverse = [1, 2, 3, 4, 5]
print("Original Stack:", stack_to_reverse)

reverse_stack(stack_to_reverse)

print("Reversed Stack:", stack_to_reverse)
