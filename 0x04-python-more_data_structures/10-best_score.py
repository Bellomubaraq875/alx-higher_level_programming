#!/usr/bin/python3
def best_score(a_dictionary):
    newDict = {}
    if a_dictionary == {} or a_dictionary is None:
        return None
    bestScore = max(a_dictionary.values())
    for key, value in a_dictionary.items():
        if value == bestScore:
            return key
