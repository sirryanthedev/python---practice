# (ex. 5.6. - Encryptie)

import os

try:
    fp = open("test.txt", "r+b")    # read and write in binary mode
except FileNotFoundError:
    print("Error: That file is not found")
except:
    print("Error: Something went wrong...")
else:
    while True:
        # read one byte, store it in buffer, break out of the loop when BYTEstring is empty
        buffer = fp.read(1) # returns a bytestring because of "b" mode
        if buffer == b"":   # if bytestring is empty, not string is empty!
            break

        fp.seek(-1, os.SEEK_CUR)    # return pointer one position for overwriting; second positional argument is equivalent to 1, i.e. relative to current pointer position

        if buffer[0] > 128:
            new = buffer[0] - 128
            fp.write(bytes([new]))  # convert new (int) to bytes
        elif ord(buffer) < 128:
            new = buffer[0] + 128
            fp.write(bytes([new]))

    fp.close()