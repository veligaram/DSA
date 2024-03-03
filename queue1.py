#Design a food ordering system where your python program will run two threads

import threading
import time

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

food_order_queue=Queue()
def place_orders(orders):
    for order in orders:
        print("placing order for :",order)
        food_order_queue.enqueue(order)
        time.sleep(0.5)
def serve_orders():
    time.sleep(1)
    while True:
        order=food_order_queue.dequeue()
        print("nowserving:",order)
        time.sleep(2)
if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']
    t1 = threading.Thread(target=place_orders, args=(orders,))
    t2 = threading.Thread(target=serve_orders)

    t1.start()
    t2.start()      
