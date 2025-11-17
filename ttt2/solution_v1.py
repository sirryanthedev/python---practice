# ----------SIMPLE CALCULATOR----------

example = input("enter expression (string): ")          # e.g.: "3 + 5 - 2**2 /2-2"

counter = 0
total = 0
current_num = ""

first = True
is_add = False
is_subtr = False
is_mult = False
is_div = False
is_pow = False

for char in example:

    if ord("0") <= ord(char) <= ord("9"):
        current_num += char

    else:
        if first and current_num != "":
            total += int(current_num)
            current_num = ""
            first = False
        elif is_add and current_num != "":
            total += int(current_num)
            current_num = ""
            is_add = False
        elif is_subtr and current_num != "":
            total -= int(current_num)
            current_num = ""
            is_subtr = False
        elif is_mult and current_num != "":
            total *= int(current_num)
            current_num = ""
            is_mult = False
        elif is_div and current_num != "":
            total /= int(current_num)
            current_num = ""
            is_div = False
        elif is_pow and current_num != "":
            total **= int(current_num)
            current_num = ""
            is_pow = False

        if char in "+-/*":
            if char == "+":
                is_add = True
            elif char == "-":
                is_subtr = True
            elif char == "*" and example[counter-1] == "*":
                is_pow = True
            elif char == "*" and example[counter+1] != "*":
                is_mult = True
            elif char == "/":
                is_div = True

    counter += 1
    if counter == len(example):
        if is_add and current_num != "":
            total += int(current_num)
        if is_subtr and current_num != "":
            total -= int(current_num)
        if is_mult and current_num != "":
            total *= int(current_num)
        if is_div and current_num != "":
            total /= int(current_num)
        if is_pow and current_num != "":
            total **= int(current_num)
        break

print(f"result: {total:.0f}")