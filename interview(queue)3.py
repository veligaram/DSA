#reversing a queue using recursion

from queue import Queue

def reverec(queue):
    if queue.qsize()<=1:
        return
    front_element=queue.get()
    reverec(queue)
    queue.put(front_element)
given_queue = Queue()
given_queue.put(1)
given_queue.put(2)
given_queue.put(3)
given_queue.put(4)
given_queue.put(5)
reverec(given_queue)
print("Reversed queue:", list(given_queue.queue))    
