# (ex. 4.6. Letterfrequencies)

def letter_count(text: str) -> int:
    """return total #letters in file

    Args:
        text (str): text in the form of a string

    Returns:
        int: number of letters
    """
    count = 0
    for char in text:
        if char.isalpha():
            count += 1
    return count

def letter_frequencies(file_1: str, file_2: str, file_3: str, file_4_csv):
    fp = open(file_1)
    text = fp.read().lower()
    freq_1 = {}
    if letter_count(text) > 0:
        for letter in "abcdefghijklmnopqrstuvwxyz":
            freq_1[letter] = text.count(letter) / letter_count(text)
    fp.close()

    fp = open(file_2)
    text = fp.read().lower()
    freq_2 = {}
    if letter_count(text) > 0:
        for letter in "abcdefghijklmnopqrstuvwxyz":
            freq_2[letter] = text.count(letter) / letter_count(text)
    fp.close()

    fp = open(file_3)
    text = fp.read().lower()
    freq_3 = {}
    if letter_count(text) > 0:
        for letter in "abcdefghijklmnopqrstuvwxyz":
            freq_3[letter] = text.count(letter) / letter_count(text)
    fp.close()

    fp = open(file_4_csv, "w")
    for letter in "abcdefghijklmnopqrstuvwxyz":
        fp.write(f"{letter},{freq_1[letter]:.5f},{freq_2[letter]:.5f},{freq_3[letter]:.5f}\n")
    fp.close()