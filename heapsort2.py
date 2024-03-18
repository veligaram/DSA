#sort a nearly sorted array using heapsort

def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arr[l] > arr[largest]:
        largest = l
    if r < n and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i] 
        heapify(arr, i, 0)
def sort_k_sorted(arr, k):
    n = len(arr)
    heap = arr[:k + 1]
    heap_sort(heap)

    index = 0
    for i in range(k + 1, n):
        arr[index] = heap[0]
        index += 1
        heap[0] = arr[i]
        heapify(heap, k + 1, 0)

    while heap:
        arr[index] = heap[0]
        index += 1
        if len(heap)==1:
            break
        heap[0] = heap.pop()
        heapify(heap, len(heap), 0)

arr = [6, 5, 3, 2, 8, 10, 9]
k = 3
sort_k_sorted(arr, k)
print("Sorted array is:", arr)
