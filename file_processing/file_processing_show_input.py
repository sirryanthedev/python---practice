# file processing - user input is placed in temp file, and once input is empty, input gets printed

fp = open("test.tmp", "w")  # open temp file in write-mode
# while user input is given, text (with newline) is appended to temp file
while True:
    text = input("Enter text: ")
    if text == "":
        break
    fp.write(f"{text}\n")
fp.close()

fp = open("test.tmp")
buffer = fp.read()
fp.close()

print(buffer)
