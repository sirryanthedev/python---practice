# write inverted contents of pc_rose.txt to pc_writetest.tmp and print them to terminal

fp = open("pc_rose.txt")    # open pc_rose.txt
buffer = fp.readlines() # creates list of all lines in pc_rose.txt
inverted = []
for line in buffer:
    inverted.append(line[::-1]) # invert lines and append them to inverted list
fp.close()  # close pc_rose.txt

fp = open("pc_writetest.tmp", "w")  # open (or create) pc_writetest.tmp in write-mode
fp.writelines(inverted)   # write all inverted lines from inverted to pc_writetest.tmp
fp.close()  # close instance of pc_writetest.tmp in write-mode

fp = open("pc_writetest.tmp")   # open pc_writetest.tmp
buffer = fp.read()  # add contents to buffer
fp.close()  # close file

print(buffer)   # print file contents to terminal
