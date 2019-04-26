import sys

elements = sys.argv[1:]
elements.sort()

for i in range(len(elements) - 1):
    if elements[i] == elements[i + 1]:
        print True
        break
else:
    print False
