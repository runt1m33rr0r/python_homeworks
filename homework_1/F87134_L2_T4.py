import sys

elements = sys.argv[1:]
elements = [int(el) for el in elements]
elements.sort()

unique_list = []

previous = None
for el in elements:
    if el != previous:
        unique_list.append(el)
    
    previous = el

print unique_list
