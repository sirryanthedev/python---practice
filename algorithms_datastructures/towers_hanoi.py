def towhanoi(n: int, source: list, target: list, spare: list) -> None:
    """imitate tower of hanoi execution recursively

    Args:
        n (int): number of disks
        source (list): source pole
        target (list): target pole
        spare (list): spare pole
    """
    # base condition: execute only if n > 0
    if n > 0:
        # move n - 1 disks from source - to spare as target - using target
        towhanoi(n-1, source, spare, target)
    
        # move nth disk (largest) from source to target
        target.append(source.pop())

        # move the n - 1 disks from spare as source - to target - using source
        towhanoi(n-1, spare, target, source)