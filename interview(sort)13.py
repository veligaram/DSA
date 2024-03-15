#sort an array in wave form

def sort_wave_array(arr):
    arr.sort()
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]

array = [3, 1, 4, 2, 5]
sort_wave_array(array)
print(array)
