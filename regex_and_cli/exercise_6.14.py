# (ex. 6.14.)

import re

pattern = r"\b[a-zA-Z']+\b" # a word has 2 boundaries, one on the left and one on the right; a words consists of letter, either uppercase or lowercase and an additional apostrophe

test = "Hello   there   234     ,       how       are you doing? It's a nice day isn't it?"

words = re.findall(pattern, test)
print(words)
