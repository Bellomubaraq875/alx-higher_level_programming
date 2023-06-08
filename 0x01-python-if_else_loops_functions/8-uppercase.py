#!/usr/bin/python3
def uppercase(str):
    Letter = ""
    for letter in str:
        if 'a' <= letter <= 'z':
            upper = chr(ord(letter) - ord('a') + ord('A'))
            Letter += upper
        elif letter == "\n" or letter == "\r":
            Letter += letter
        else:
            Letter += letter
    print("{}".format(Letter))
