#!/usr/bin/python3
def pow(a, b):
    exe = 0
    if a < 0:
        a *= -1
    exe = 1
    pow = a ^ b
    if exe == 1:
        pow = a ^ b
    return pow
