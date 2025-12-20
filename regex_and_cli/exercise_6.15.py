# (ex. 6.15)

import re

text = "De zonsondergang is prachtig. Dat is de waarheid. De zon komt des morgens terug op."

# find all instances of the word: "de"
pattern = r"\b(de)\b"

de_list = re.findall(pattern, text, re.I) # create a list of all instances of "de", flag re.I to ignore case

print(de_list)