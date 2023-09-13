#!/usr/bin/python3
"""task 7"""


import json
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


filename = "add_item.json"

try:
    listJ = load_from_json_file(filename)
except Exception:
    listJ = []

for index in range(1, len(sys.argv)):
    listJ.append(sys.argv[index])
save_to_json_file(listJ, filename)
