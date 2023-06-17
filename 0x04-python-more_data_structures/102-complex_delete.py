#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    newDict = []
    for key, v in a_dictionary.items():
        if v is value:
            newDict.append(key)
    for i in newDict:
        del a_dictionary[i]
    return(a_dictionary)
