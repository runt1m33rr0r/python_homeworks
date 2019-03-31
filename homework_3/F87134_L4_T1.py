import sys

input = sys.argv[1:]
value = input[0]

d = { 1:'a', 2:'b', 3:'c', 4:'a', 5:'d', 6:'e', 7:'a', 8:'b' }
result = [key for key in d if d.get(key) == value]

print result
