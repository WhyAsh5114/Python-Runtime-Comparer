import time
from numpy import array

f = open('input.txt', 'r')
data = f.read()
f.close()
array = array([int(x) for x in data.split()])
size = len(array)
start_time = time.time()

for ind in range(size):
    min_index = ind
    for j in range(ind + 1, size):
        if array[j] < array[min_index]:
            min_index = j
    (array[ind], array[min_index]) = (array[min_index], array[ind])


end_time = time.time()
f = open('output.txt', 'w+')
f.write(str(end_time - start_time))
f.close()
