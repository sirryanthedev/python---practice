# (ex. 3.3.)

def hamming_dist(str1: str, str2: str) -> int:
    """return hamming distance between 2 strings

    Args:
        str1 (str): first string
        str2 (str): second string

    Returns:
        int: number of different characters
    """
    len_diff = abs(len(str1) - len(str2))
    total_diff = len_diff
    
    if len(str1) > len(str2):
        greater, lesser = str1, str2
    else:
        greater, lesser = str2, str1
    
    for index, value in enumerate(lesser):
        if lesser[index] != greater[index]:
            total_diff += 1
    return total_diff

def hd_bin_combinations(k: int, s: str, current = "") -> None:
    """binary combinations (0's and 1's) of length s, 
    when hamming distance between combination and s <= k

    Args:
        k (int): max. number of different characters - hamming distance output
        s (str): bitstring used for comparison
        current (str, optional): buffer for building the combinations. Defaults to "".
    """
    if len(current) == len(s):
        if hamming_dist(current, s) <= k:
            print(current, end=" ")
        return
    
    for option in "01":
        hd_bin_combinations(k, s, current + option)

# function call with k = 2, and s = "0000":
# hd_bin_combinations(2, "0000")

# output:
# 0000 0001 0010 0011 0100 0101 0110 1000 1001 1010 1100 