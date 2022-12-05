from random import randint
from tqdm import tqdm

data = ""
for i in tqdm(range(1, 11)):
    for i in range(100000 * i):
        data += str(randint(0, 1000)) + " "
    data += "\n"

f = open('allInputs.txt', 'w+')
f.write(data)
f.close()
