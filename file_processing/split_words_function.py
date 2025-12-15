def split_words(text: str) -> list[str]:
    """return a list of words from a string

    Args:
        text (str): input string

    Returns:
        list[str]: list of words from input string
    """
    words = []  # list of words
    current = ""    # buffer of characters being read currently

    # loop through every character in given string
    for ch in text:
        if ch.isalpha():    # if character is of type alpha, add it to current
            current += ch
        else:   # if character is not of type alpha:
            if current: # if current has a length (is not empty):
                words.append(current)   # add whatever is in current to words
                current = ""    # empty current

    if current: # if, at the end, anything left in buffer:
        words.append(current)   # add current content to words

    return words