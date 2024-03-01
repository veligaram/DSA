#Write a function in python that can reverse a string using stack data structure.

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
def reverse_string(string):
    s=Stack()
    for ch in string:
        s.push(ch)
    res=''
    while s.size()!=0:
        res +=s.pop()
    return res
if __name__=='__main__':
    print(reverse_string("hi!, Iam Devanandh Veligaram"))
    print(reverse_string("you know me"))
          

