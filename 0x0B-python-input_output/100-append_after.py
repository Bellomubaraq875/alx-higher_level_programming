#!/usr/bin/python3
"""
task 13
"""


def append_after(filename="", search_string="", new_string=""):
    """This function appends "new_string" after a line containing
    "search_string" in "filename" """
    with open(filename, "r", encoding='utf-8') as afile:
        lineList = []
        while True:
            line = afile.readline()
            if line == "":
                break
            lineList.append(line)
            if search_string in line:
                lineList.append(new_string)
    with open(filename, "w", encoding='utf-8') as afile:
        afile.writelines(lineList)
