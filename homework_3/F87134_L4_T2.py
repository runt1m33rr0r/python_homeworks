import sys

input = sys.argv[1:]
text = input[0]

histogram = {}
for let in text:
    if histogram.get(let) == None:
        histogram[let] = 1
    else:
        histogram[let] += 1

print sorted(histogram.items())

