#using class and functions to implement stack and its operations
from collections import deque

class Stack:
    def __init__(self):
        self.container=deque()
    def push(self,val):
        self.container.append(val)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def is_empty(self):
        return len(self.container)==0
    def size(self):
        return len(self.container)
    
s=Stack()
s.push(5)
s.push(10)
s.push(7)
print(s.peek())
print(s.size())
s.pop()
s.pop()
s.pop()
print(s.is_empty())


