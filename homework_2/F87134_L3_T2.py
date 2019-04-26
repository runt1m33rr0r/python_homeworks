import sys
import string

input = sys.argv[1:]
text = input[0].strip().upper().translate(string.maketrans('', ''), string.punctuation)
key = input[1].strip().upper().translate(string.maketrans('', ''), string.punctuation)

# extend the key
initial_len = len(key)
current_letter = 0;
while len(key) < len(text):
    key += key[current_letter]
    current_letter = (current_letter + 1) % initial_len

# encode the text
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
result = []
for text_let, key_let in zip(text, key):
    key = alphabet.index(key_let)
    encoded = alphabet[(alphabet.index(text_let) + key) % len(alphabet)]
    result.append(encoded)

print ''.join(result)

