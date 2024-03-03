#implementation of queue using class and functions
from collections import deque

class Queue:
    def __init__(self):
        self.buffer=deque()
    def enqueue(self,val):
        self.buffer.appendleft(val)
    def dequeue(self):
        return self.buffer.pop()
    def is_empty(self):
        return len(self.buffer)==0
    def size(self):
        return len(self.buffer)
q=Queue()
q.enqueue(5)
q.enqueue(8)
q.enqueue(27)
print(q)
print(q.dequeue())
print(q.is_empty())
