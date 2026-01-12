from itertools import * # import the entire itertools lib

word = input("Enter a word: ") # ask the user for input - a word

for item in permutations(word): # create all permutations of word
    print(''.join(item)) # actually form words of the individual letters in the permutation