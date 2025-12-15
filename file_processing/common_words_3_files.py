# (ex. 4.5.)

def split_words(file: str) -> list:
    """return list of words from a string

    Args:
        file (str): source string

    Returns:
        list: words from source
    """
    current = ""    # buffer in which the current alpha characters are placed
    words = []  # list of individual words

    for char in file: # loop through all characters:
        if char.isalpha():  # if character is of type alpha:
            current += char # add it to buffer
        else:   
            if current: # if character isn't of type alpha and current not empty:
                words.append(current)   # add whatever is in current to words
                current = ""    # clear current
    
    if current: # if anyting left in buffer after loop:
        words.append(current)   # add remaining characters (word) in list

    return words

def common_words(file_1: str, file_2: str, file_3: str) -> set(str):
    """return common words between 3 files

    Args:
        file_1 (_type_): string

    Returns:
        _type_: set of common words
    """
    fp = open(file_1)
    buffer = fp.read()
    buffer = buffer.lower()
    fp.close()
    words_file_1 = set(split_words(buffer))

    fp = open(file_2)
    buffer = fp.read()
    buffer = buffer.lower()
    fp.close()
    words_file_2 = set(split_words(buffer))

    fp = open(file_3)
    buffer = fp.read()
    buffer = buffer.lower()
    fp.close()
    words_file_3 = set(split_words(buffer))

    return words_file_1 & words_file_2 & words_file_3