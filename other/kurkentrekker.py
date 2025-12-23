# (ex. kurkentrekker - Dodona)

def rotatie_links(number: int) -> int:
    number = str(number)
    return int(number[1:] + number[:1])

def rotatie_rechts(number: int) -> int:
    number = str(number)
    return int(number[-1] + number[:-1])

def parasitisch(number: int) -> int:
    for n in range(1,10):
        if n * number == rotatie_rechts(number):
            return n
    return 0

def kurkentrekker(n: int, k: int) -> int:
    if k < n:
        raise ValueError("k must be greater or equal to n")

    # digits will be stored least-significant first
    digits = [k]
    carry = 0

    while True:
        total = n * digits[-1] + carry
        digit = total % 10
        carry = total // 10

        if digit == k and carry == 0:
            break

        digits.append(digit)

    # build the integer once, at the end
    result = 0
    for d in reversed(digits):
        result = result * 10 + d

    return result