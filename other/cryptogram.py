# (ex. cryptogrammen - Dodona)

def cryptogram(assignment, solution) -> str:
    # len(assignment) is the same as len(solution)
    if len(assignment) != len(solution) or len(assignment) == 0:
        print("both input strings should have the same length > 0!")
        return None

    # initialize mapping dictionairies for lower -and uppercase letters
    mapping_lower = {}
    mapping_upper = {}

    for i in range(len(assignment)):
        # condition: if characters in both strings are letters
        if assignment[i].isalpha() and solution[i].isalpha():
            # add lower -and uppercase letters to appropriate mapping dicts
            mapping_lower[assignment[i].lower()] = solution[i].lower()
            mapping_upper[assignment[i].upper()] = solution[i].upper()
    # merge both dicts together to create a main dict called mapping
    mapping = mapping_lower | mapping_upper

    # initialize an empty result string to store the end result
    result = ""
    for i in range(len(solution)):
        # if character in second string at index i is a letter: add it to result
        if solution[i].isalpha():
            result += solution[i]
        # if character in second string at index i is "?": perform a check
        elif solution[i] == "?" and assignment[i] in mapping:
            # if character in first string at index i is mapped: add the equivalent value to result
            result += mapping[assignment[i]]
        # otherwise: just append the character to result
        else:
            result += solution[i]

    return result
