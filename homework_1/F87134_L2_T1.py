import sys

input = sys.argv[1:]

for i in range(len(input) - 1):
    if input[i] > input[i + 1]:
        print("unsorted")
        break
else:
    print("sorted")
