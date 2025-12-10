# (ex. 4.4 - Dodona) swap 2 variables without using a 3rd variable

a = 25;
b = 15;

print(f"Before\na: {a}\nb: {b}\n\n")

a += b
b = a - b
a -=b

print(f"After\na: {a}\nb: {b}")
