def fac():
    """print 1!, 2!, 3!,..., 10!

    Yields:
        _type_: faculty (x!) where x is a number (1-10)
    """
    num = 1
    current = 1
    while num <= 10:
        current *= num
        num += 1
        yield current

for fac in fac():
    print(fac)