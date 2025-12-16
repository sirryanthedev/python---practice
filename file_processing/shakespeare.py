# (ex. 4.9. - Shakespeare)

def split_words(text: str) -> list:
    buffer = ""
    words = []

    for char in text:
        if char.isalpha():
            buffer += char
        else:
            if buffer:
                words.append(buffer)
                buffer = ""
    if buffer:
        words.append(buffer)

    return words

with open("shakespeare.txt") as fp:
    buffer = ""
    words_list = []
    nsentences = 0
    the_count = 0

    for line in fp:
        for char in line:
            if char == ".":
                words_list = split_words(buffer.lower())
                buffer = ""
                nsentences += 1
                the_count += words_list.count("the")
            else:
                buffer += char

    print(f"#occurences \"the\": {the_count}\noccurence \"the\" per sentence: {the_count / nsentences:.2f}")
