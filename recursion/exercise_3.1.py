# (ex. 3.1.)

def dna_combinations(n: int, current = ""):
    # if combination length is equal to input length, print combination and return
    if len(current) == n:
        print(current)
        return
    # per loop in which there is no return, add an option to current, and call the function recursively
    for option in "ACGT":
        dna_combinations(n, current + option)

# function call to get all "ACGT" combinations with length 2
dna_combinations(2)