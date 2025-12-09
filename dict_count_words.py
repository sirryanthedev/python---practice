# (ex. 4.3. count words)

import re

def split_words(filepath: str) -> list:
    """split text into words, return a list of those words

    Args:
        filepath (str): filepath containing the (text)file

    Returns:
        list: individual words of the original file
    """
    fp = open(filepath)
    text = fp.read()
    text = text.lower() # convert read text to lowercase
    fp.close()

    words = re.split(r"[^a-zA-Z]+", text) # split text into words (r for raw; ^ stands for "not"; + stands for "one or more")

    # words will probably contain empty spaces, so return word for word in the list of words if word has a length and thus isn't empty
    return [word for word in words if word]

def count_words(filepath: str) -> dict:
    """return dict of words and #times they appear

    Args:
        filepath (str): filepath containing the (text)file

    Returns:
        dict: key = word; value = count
    """
    words = split_words(filepath)
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1 # update the dictionary as you go instead of scanning the entire list each time like this: count[w] = words.count(w)
    return count