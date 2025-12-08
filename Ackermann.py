# (ex. 2.5. Ackermann function)

def ackermann(m: int, n: int) -> int:
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return ackermann(m - 1, ackermann(m, n - 1))

# Ackermann function principles/definition
# A(m, n) = (n + 1) if m == 0
# A(m, n) = (A(m - 1, 1)) if m > 0 and n == 0
# A(m, n) = (A(m - 1, A(m, n - 1))) if n > 0 and m > 0