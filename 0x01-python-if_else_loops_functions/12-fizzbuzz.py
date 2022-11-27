#!/usr/bin/python3
def fizzbuzz():
    for x in range (1,101):
        if x%15 == 0:
            print("{:s}".format("fizzbuzz"), end = " ")
        elif x%5 == 0:
            print ("{:s}".format("buzz"), end = " ")
        elif x%3 == 0:
            print("{:s}".format("buzz"), end = " ")
        else :
            print("{:d}".format(x), end = " ")
