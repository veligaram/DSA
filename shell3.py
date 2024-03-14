#Given a list of tuples where each tuple contains a student's name and
#their corresponding score,sort the list based on scores in ascending order using shell sort.

def shellsortscores(students):
    n = len(students)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = students[i]
            j = i
            while j >= gap and students[j - gap][1] > temp[1]:
                students[j] = students[j - gap]
                j -= gap
            students[j] = temp
        gap //= 2
students = [("Alice", 85), ("Bob", 72), ("Charlie", 91), ("David", 68)]
shellsortscores(students)
print("Sorted list of students based on scores:", students)
