#find pairs with givem sum in doubly linked list

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

def findPairsWithSum(head, x):
    start = head
    end = head
    while end.next is not None:
        end = end.next

    pairs_found = False

    while start != end and start.data <= end.data:
        current_sum = start.data + end.data

        if current_sum == x:
            print("Pair found: ({}, {})".format(start.data, end.data))
            pairs_found = True
            start = start.next
            end = end.prev
        elif current_sum < x:
            start = start.next
        else:
            end = end.prev

    if not pairs_found:
        print("No pairs found with the given sum.")
head = Node(1)
head.next = Node(2)
head.next.prev = head
head.next.next = Node(4)
head.next.next.prev = head.next
head.next.next.next = Node(5)
head.next.next.next.prev = head.next.next
head.next.next.next.next = Node(6)
head.next.next.next.next.prev = head.next.next.next
head.next.next.next.next.next = Node(8)
head.next.next.next.next.next.prev = head.next.next.next.next
head.next.next.next.next.next.next = Node(9)
head.next.next.next.next.next.next.prev = head.next.next.next.next.next
        
findPairsWithSum(head, 10)
