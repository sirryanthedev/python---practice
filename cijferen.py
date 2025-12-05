# (ex. 5.7 - Dodona) Cijferen

number_1 = int(input("Enter the first number: "))
number_2 = int(input("Enter the second number: "))
number_3 = int(input("Enter the third number: "))

sum = number_1 + number_2 + number_3

width = len(str(sum)) + 2

print(f"{number_1:>{width}}")
print(f"+ {number_2:>{width - 2}}")
print(f"+ {number_3:>{width - 2}}")

print("-" * width)

print(f"= {sum:{width-2}}")

# Read three natural numbers as input. Then print them in a way that mimics manual column addition.

# All numbers, including the final result, must be printed below each other, right-aligned. In addition, a plus sign (+) should be placed in front of the second and third number, and an equals sign (=) in front of the result. A horizontal line should be drawn between the input numbers and the result.