# (ex. caucasus - Dodona)

def occurrences(str_1: str) -> dict:
    str_1 = str_1.lower()
    dict_chars = {}
    
    for char in str_1:
        if char.isalpha():
            dict_chars[char] = str_1.count(char)
    return dict_chars

def balanced(str_1: str) -> bool:
    first = True
    dict_chars = occurrences(str_1)
    number = 0

    for value in dict_chars.values():
        if first:
            number = value
            first = False
        elif value != number or value < 2:
            return False
    return True

# We say a word is balanced if all its letters have the same number of occurrences. For example, the word Caucasus contains four pairs of letters and the word SCINTILLESCENT contains seven pairs of letters.

# scintillescent

# Assignment
# Write a function occurrences that takes a string 
#  (str). The function must return a dictionary (dict) that maps each letter (str) in 
#  onto the number of occurrences (int) of that letter in 
# . All characters in 
#  that are no letter must be ignored. In counting the number of occurrences of a letter, no distinction must be made between uppercase and lowercase letters. The returned dictionary must use lowercase letters as its keys.

# Write a function balanced that takes a string 
# . The function must return a Boolean value (bool) that indicates whether each letter occurs a fixed number of times 
#  in 
# , with 
# . Counting the number of occurrences of the letters in 
#  must be done in the same way as in the function occurrences.

# Example
# >>> occurrences('Caucasus')
# {'a': 2, 'c': 2, 'u': 2, 's': 2}
# >>> occurrences('teammate')
# {'a': 2, 'm': 2, 'e': 2, 't': 2}
# >>> occurrences('SCINTILLESCENT')
# {'c': 2, 'e': 2, 'i': 2, 'l': 2, 'n': 2, 's': 2, 't': 2}
# >>> occurrences('chachacha')
# {'a': 3, 'h': 3, 'c': 3}
# >>> occurrences('blahblahblahblah')
# {'a': 4, 'h': 4, 'b': 4, 'l': 4}
# >>> occurrences('intestine')
# {'i': 2, 's': 1, 'e': 2, 't': 2, 'n': 2}

# >>> balanced('Caucasus')
# True
# >>> balanced('teammate')
# True
# >>> balanced('SCINTILLESCENT')
# True
# >>> balanced('lysosome')
# False
# >>> balanced('intestines')
# True
# >>> balanced('mesosome')
# True
