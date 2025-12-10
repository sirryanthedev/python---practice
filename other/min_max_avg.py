# (ex. 5.5 - Dodona) output minimum, maximum and average of 3 given numbers

total = 0;

for i in range(3):

    x = int(input(f"Enter number {i + 1}: "))
    total += x

    if i == 0:
        max = x
        min = x

    if x > max:
        max = x
    if x < min:
        min = x

print(f"maximum: {max}\nminimum: {min}\naverage: {total/3:.2f}")
