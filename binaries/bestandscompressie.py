# (ex. 5.9. - Bestandscompressie)
# this exercise has logic which is based on the previous exercise (compressie_decompressie)

from compressie_decompressie import compress, decompress # functions from the file compressie_decompressie.py
from os.path import exists

# keep asking for input until conditions are met
while True:
    in_file = input("> Input file: ")
    out_file = input("> Output file: ")

    if exists(in_file) and not exists(out_file):
        break

    print("\nThe input file must exist!\nThe output file can't exist beforehand.\nTry again...\n")

# keep asking for input until a possible choice is made
while True:
    choice = input("Do you want to compress or decompress: ")

    if choice.lower() == "compress":
        with open(in_file) as fp:
            buffer = fp.read()
        compressed = compress(buffer)
        with open(out_file, "wb") as fp:
            fp.write(compressed)
        print("You successfully compressed {} into {}".format(in_file, out_file))
        break

    elif choice.lower() == "decompress":
        with open(in_file, "rb") as fp:
            buffer = fp.read()
        decompressed = decompress(buffer)
        with open(out_file, "w") as fp:
            fp.write(decompressed)
        print("You successfully decompressed {} into {}".format(in_file, out_file))
        break

    else:
        print("Enter a valid choice (compress - decompress)")
        continue
