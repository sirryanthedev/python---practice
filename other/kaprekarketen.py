# (ex. kaprekarketen - Dodona)

def kaprekarketen(n: int) -> list:
    num_list = [n]

    while True:
        sorted_descending = ""
        sorted_ascending = ""

        for digit in sorted(str(num_list[-1]), reverse=True):
            sorted_descending += digit

        for digit in sorted(str(num_list[-1])):
            sorted_ascending += digit

        next_number = int(sorted_descending) - int(sorted_ascending)

        if next_number in num_list:
            break

        num_list.append(next_number)

        if next_number == 0:
            break

    return num_list