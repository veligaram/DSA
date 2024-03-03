#implementation of queue using deque

from collections import deque
q=deque()
q.appendleft(5)
q.appendleft(8)
q.appendleft(26)
print(q)
print("///////////")
q.pop()
print(q)
print("///////////")
q.pop()
print(q)
print("///////////")
q.pop()
print(q)
print("///////////")
