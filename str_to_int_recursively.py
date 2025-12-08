# (ex. 2.9. String to integer - Dodona)
def convert(s: str) -> int:
    # base case: single digit
    if len(s) == 1:
        return ord(s[0]) - ord('0')
    
    # recursive case
    return ((ord(s[0]) - ord('0')) * (10 ** (len(s) - 1)) + convert(s[1:]))