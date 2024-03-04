#reversing the first k elements of a queue

from queue import Queue

def reverse_k_elements(queue, k):
    if k <= 0 or k > queue.qsize():
        print("Invalid value of k.")
        return

    stack = []
    for _ in range(k):
        stack.append(queue.get())
    while stack:
        queue.put(stack.pop())
    for _ in range(queue.qsize() - k):
        queue.put(queue.get())

given_queue = Queue()
given_queue.put(1)
given_queue.put(2)
given_queue.put(3)
given_queue.put(4)
given_queue.put(5)

k_value = 3

print(list(given_queue.queue))
reverse_k_elements(given_queue, k_value)
print(list(given_queue.queue))
