def no_vowels(sourcefile: str, destfile: str) -> tuple:
    """write source file contents to destination file, but without vowels

    Args:
        sourcefile (str): file to write from
        destfile (str): file to be written to

    Returns:
        tuple: first element: total #characters in source file
               second element: #characters written to destination file
    """
    fp = open(sourcefile)
    current = ""
    vowels = "aeuioAEUIO"
    transfer_count = 0  # keep track of #characters copied from source file to destination file
    total_count = 0 # keep track of total #characters in source file
    while True:
        buffer = fp.readline()
        if buffer == "":
            break
        for char in buffer:
            if char not in vowels:
                current += char
                transfer_count += 1
            total_count += 1
    fp.close()

    fp = open(destfile, "w")
    fp.write(current)
    fp.close()

    info = (total_count, transfer_count)
    return info