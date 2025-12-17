# (ex. 5.7. - Compressie and ex. 5.8. - Decompressie)

import math

def compress(filecontents: str) -> bytes:
    base = "etaoinshrdlcum "
    half_bytes = []
    bytes_list = []

    for char in filecontents:
        if char in base:
            half_bytes.append(base.find(char) + 1)
        else:
            half_bytes.append(0)
            half_bytes.append(math.floor(ord(char) / 16))
            half_bytes.append(ord(char) % 16)

    result = 0

    for i in range(len(half_bytes)):
        if i % 2 == 0:
            result += half_bytes[i] * 16
        else:
            result += half_bytes[i]
            bytes_list.append(result)
            result = 0
    if result:
        bytes_list.append(result)

    return bytes(bytes_list)

def decompress(filecontents: bytes) -> str:
    base = "etaoinshrdlcum "
    bytes_list = []
    half_bytes = []
    original = ""

    for byte in filecontents:
        bytes_list.append(byte)

    for byte in bytes_list:
        half_bytes.append(byte // 16)
        half_bytes.append(byte % 16)
    
    i = 0
    while i < len(half_bytes):
        if half_bytes[i] == 0 and (i + 2 < len(half_bytes)):    # if there are two following numbers after 0, do the following:
            original += (chr(half_bytes[i+1] * 16 + (half_bytes[i+2])))
            i += 3
        else:   # if the current number isn't 0, or there aren't two numbers after it, do the following:
            if half_bytes[i] != 0:  # if current number isn't 0, do this, else, do nothing (we assume that a 0 always has 2 following numbers, if not, 0 is seen as a garbage value which can't be used)
                original += base[half_bytes[i] - 1] # if half_bytes at i were 0, we would try to find base[-1], which would generate an error
            i += 1  # in both cases (half_bytes[i] == 0 or half_bytes[i] != 0): always increment to avoid being stuck in the loop

    return original

# test:
# a = compress("Hello, world!")
# print(a)
# print(decompress(a))