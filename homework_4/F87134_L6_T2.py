import sys

user_input = sys.argv[1:]
number = int(user_input[0])
power = int(user_input[1])


def pow(num, result_num, power):
    if power == 1:
        return result_num
    if power == 0:
        return 1

    return pow(num, result_num * num, power - 1)


print pow(number, number, power)