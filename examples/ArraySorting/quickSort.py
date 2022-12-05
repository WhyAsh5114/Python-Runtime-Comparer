import time
from numpy import array

f = open('input.txt', 'r')
data = f.read()
f.close()
data = array([int(x) for x in data.split()])
start_time = time.time()

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            (array[i], array[j]) = (array[j], array[i])

    (array[i + 1], array[high]) = (array[high], array[i + 1])
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)

quickSort(data, 0, len(data) - 1)

end_time = time.time()
f = open('output.txt', 'w+')
f.write(str(end_time - start_time))
f.close()
