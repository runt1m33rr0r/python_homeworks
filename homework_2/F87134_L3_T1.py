import sys
import string

input = sys.argv[1:]
text = input[0].strip().upper().translate(string.maketrans('', ''), string.punctuation)
key = int(input[1])

alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
encoded = ''.join([alphabet[(alphabet.index(let) + key) % len(alphabet)] for let in text])

print encoded
