# (ex. 6.17 - unix-like grep functionality through cli)

import re, sys, os, os.path

folder = os.getcwd()
contents = os.listdir(folder)

if len(sys.argv) > 2:
    pattern = sys.argv[1]
    extension = sys.argv[2]
else:
    sys.exit(1)

found = False

for file in contents:
    if file.endswith(f".{extension}"):
        with open(file) as fp:
            line = 0
            while True:
                buffer = fp.readline()
                line += 1
                if buffer == "":
                    break
                mlist = re.finditer(pattern, buffer)
                for m in mlist:
                    print(f"{file}:{line}:{m.group()}")
                    found = True
if not found:
    print("No matches found.")