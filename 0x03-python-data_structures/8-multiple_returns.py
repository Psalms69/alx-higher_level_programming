#!/usr/bin/python3
def multiple_returns(sentence):
    length = len(sentence)
    first = sentence[0] if length > 0 else "none"
    tup =(first, length)
    return (tup) 
