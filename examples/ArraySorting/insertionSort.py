import time
from numpy import array

f = open('input.txt', 'r')
data = f.read()
f.close()
data = array([int(x) for x in data.split()])
start_time = time.time()

for i in range(1, len(data)):
    key = data[i]
    j = i - 1
    while j >= 0 and key < data[j]:
            data[j+1] = data[j]
            j -= 1
    data[j+1] = key

end_time = time.time()
f = open('output.txt', 'w+')
f.write(str(end_time - start_time))
f.close()
