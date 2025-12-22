# (ex. mysterieuze slogan - Dodona)

def solve_slogan(sentence: str, start: int, step: int) -> str:
    pos = start
    result = ""

    for _ in range(len(sentence)):
        result += (sentence[pos % len(sentence)])
        pos += step

    return result

sentence = input("Enter a sentence: ")
start = input("Enter a starting index: ")
step = input("Enter a step width: ")

try:
    start = int(start)
except ValueError:
    print("The starting index must be of type int!")
except:
    print("Something went wrong...")

try:
    step = int(step)
except ValueError:
    print("The step width must be of type int!")
except:
    print("Something went wrong...")

print(solve_slogan(sentence, start, step))