#!/usr/bin/python3
def multiple_returns(sentence):
    lEngth = len(sentence)
    if lEngth < 1:
        firstcharacter = None
    else:
        firstcharacter = sentence[0]
    return lEngth, firstcharacter
