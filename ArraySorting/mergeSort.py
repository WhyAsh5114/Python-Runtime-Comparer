import time
from numpy import array, sort

f = open('input.txt', 'r')
data = f.read()
f.close()
data = array([int(x) for x in data.split()])
start_time = time.time()


sort(data, kind='mergesort')

end_time = time.time()
f = open('output.txt', 'w+')
f.write(str(end_time - start_time))
f.close()
