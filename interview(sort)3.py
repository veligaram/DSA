#check if any two intervals intersects among a given set of intervals

def intervals_overlap(intervals):
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    for i in range(1, len(sorted_intervals)):
        if sorted_intervals[i][0] < sorted_intervals[i-1][1]:
            return True 
    
    return False  
arr1 = [(1, 3), (5, 7), (2, 4), (6, 8)]
arr2 = [(1, 3), (7, 9), (4, 6), (10, 13)]

print("Output:", intervals_overlap(arr1))
print("Output:", intervals_overlap(arr2))
