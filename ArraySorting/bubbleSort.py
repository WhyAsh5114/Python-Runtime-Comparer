import time
from numpy import array

f = open('input.txt', 'r')
data = f.read()
f.close()
data = array([int(x) for x in data.split()])
start_time = time.time()

for i in range(len(data)):
    swaps_performed = 0
    for j in range(len(data) - 1):
        if data[i] < data[i+1]:
            data[i], data[i+1] = data[i+1], data[i]
            swaps_performed += 1
    if swaps_performed == 0:
        break

end_time = time.time()
f = open('output.txt', 'w+')
f.write(str(end_time - start_time))
f.close()
