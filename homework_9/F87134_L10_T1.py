import sys


input = sys.argv[1:]
input_file_name = input[0]
output_file_name = input[1]

try:
    lines = []
    with open(input_file_name) as input:
        lines = input.readlines()

    if lines[-1][-1] != '\n':
        lines[-1] += '\n'

    lines.sort()

    with open(output_file_name, 'w', True) as output:
        output.writelines(lines)
except:
    pass