#sort numbers on different machines

import heapq

def merge_sorted_machines(machines):
    heap = []
    for i, machine in enumerate(machines):
        if machine:  
            heapq.heappush(heap, (machine[0], i, 0))    
    merged_list = []
    while heap:
        smallest, machine_index, index_in_machine = heapq.heappop(heap)
        merged_list.append(smallest)
        if index_in_machine + 1 < len(machines[machine_index]):
            next_number = machines[machine_index][index_in_machine + 1]
            heapq.heappush(heap, (next_number, machine_index, index_in_machine + 1))
    
    return merged_list
machines = [
    [30, 40, 50],
    [35, 45],
    [10, 60, 70, 80, 100]
]

print("Output:", merge_sorted_machines(machines))
