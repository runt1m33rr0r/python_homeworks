import sys

user_input = sys.argv[1:]
start = int(user_input[0])
end = int(user_input[1])
numbers = [-1] * end;


def fib(num):
    if numbers[num] != -1:
        return numbers[num]

    if num < 2:
        numbers[num] = num
    else:
        numbers[num] = fib(num - 1) + fib(num - 2)
    
    return numbers[num]


fib(end - 1)
print numbers[start - 1 : end]