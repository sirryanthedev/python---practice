# (ex. 2.7. gcd recursively)

def gcd(a: int, b: int):
    if a % b == 0:
        return b
    elif b % a == 0:
        return a
    if a > b:
        greatest = a
        least = b
    else:
        greatest = b
        least = a
    return gcd(least, greatest % least)