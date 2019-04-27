import sys


input = sys.argv[1:]
file_name = input[0]
searched_word = input[1]

lines = []
with open(file_name) as f:
    lines = f.readlines()

dictionary = {}
for line in lines:
    key, word = line.split(':')
    word = word.rstrip()
    key = key.rstrip()

    dictionary[key] = word

found = dictionary.get(searched_word)
if found:
    print found