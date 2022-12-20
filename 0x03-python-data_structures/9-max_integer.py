#!/usr/bin/python3
def max_integer(my_list=[]):
       max_value = None
       for number in my_list :
           if max_value is None or max_value < number:
               max_value = number
               print(max_value)
