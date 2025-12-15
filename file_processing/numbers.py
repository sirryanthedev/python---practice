# (ex. 4.7. - a and b)

import random

n = 10

for num in range(1,n):
    fp = open(f"{num}.text", "w")
    numbers = "\n".join([str(random.randint(1,1000)) for _ in range(10)])
    fp.write(numbers)
    fp.close()

tot = open("all_numbers", "a")
for num in range(1,n):
    fp = open(f"{num}.text")
    tot.write(fp.read() + "\n\n")
    fp.close()
tot.close()