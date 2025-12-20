# (ex. 6.18)

import re

def sum_snumbers(text: str) -> float:
    result = 0

    pattern = r"-?\d+(?:[,.]?\d+)?" # second "?" in "?:" for non-capturing group, last "?" for optional decimal part
    numlist = re.findall(pattern,text)
    
    for num in numlist:
        if "," in num:
            num = num.replace(",", ".")
        result += float(num)

    return result