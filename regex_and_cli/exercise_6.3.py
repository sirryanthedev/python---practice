# (ex. 6.3.)

import sys

sum = 0
i = 1

while i < len(sys.argv):
    try:
        num = int(sys.argv[i])
    except ValueError:
        print("Arguments must be numbers!")
        sys.exit(1)
    except:
        print("Something went wrong...")
        sys.exit(1)
    else:
        sum += num
    i += 1

print(f"Sum: {sum}")