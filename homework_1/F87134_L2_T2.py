import sys

input = sys.argv[1:]
first = sorted(input[0].lower())
second = sorted(input[1].lower())

if first == second:
    print True
else:
    print False
