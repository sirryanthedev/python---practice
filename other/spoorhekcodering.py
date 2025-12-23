# (ex. spoorhekcodering - Dodona)

# Encoding = zigzag write → row read
# Decoding = row write → zigzag read

def zigzag_numbers(length: int, upper_limit: int) -> list:
    line = 0
    num = 0
    ascend = False
    descend = False
    r_list = []

    while line < length:
        if num == 0:
            descend = False
            ascend = True
        if ascend:
            r_list.append(num)
            line += 1
            num += 1
        if num == (upper_limit - 1):
            ascend = False
            descend = True
        if descend:
            r_list.append(num)
            line += 1
            num -= 1

    return r_list

def codeer(message: str, num_rails: int = 1) -> str:
    encoded_message = ""
    rails = []
    
    if num_rails == 1:
        return message

    for _ in range(num_rails):
        rails.append(["#" for _ in range(len(message))])

    r_list = zigzag_numbers(len(message), num_rails)

    # zigzag-writing
    for idx in range(len(message)):
        zigzag_number = r_list[idx]
        rails[zigzag_number][idx] = message[idx]

    for row in rails:
        for char in row:
            if char != "#":
                encoded_message += char

    return encoded_message

def decodeer(encoded_message: str, used_rails: int = 1) -> str:
    decoded_message = ""
    length = len(encoded_message) # constant length instead of len(encoded_message) which changes during execution
    rails = []

    if used_rails == 1:
        return encoded_message

    for _ in range(used_rails):
        rails.append(["#" for _ in range(length)])

    r_list = zigzag_numbers(length, used_rails)

    # filling zigzag pattern with string flag "value"
    for idx in range(length):
        zigzag_number = r_list[idx]
        rails[zigzag_number][idx] = "value"

    # row writing
    for row in range(used_rails):
        for col in range(length):
            if rails[row][col] == "value":
                rails[row][col] = encoded_message[0]
                encoded_message = encoded_message[1:]

    # zigzag-reading
    for idx in range(length):
        zigzag_number = r_list[idx]
        decoded_message += rails[zigzag_number][idx]

    return decoded_message