#!/usr/bin/python3
def print_last_digit(number):
    last = number%10
    if number < 0:
        number *= -1
    else:
         last = last
    print("{:d}".format(last), end ="")
    return (last)
