#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except (TypeError, ValueError) as errorm:
        print("Exception: {}".format(errorm), file=sys.stderr)
        return False
