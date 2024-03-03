#implement stack using queues

from queue import Queue

class StackUsingQueue:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, item):
        self.queue1.put(item)

    def pop(self):
        while self.queue1.qsize() > 1:
            self.queue2.put(self.queue1.get())
        if not self.queue1.empty():
            popped_item = self.queue1.get()
            self.queue1, self.queue2 = self.queue2, self.queue1

            return popped_item
        else:
            return None  
    def is_empty(self):
        return self.queue1.empty() and self.queue2.empty()

    def size(self):
        return self.queue1.qsize() + self.queue2.qsize()

stack = StackUsingQueue()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Popped item:", stack.pop())
print("Stack size after pop:", stack.size())
print("Is the stack empty?", stack.is_empty())
