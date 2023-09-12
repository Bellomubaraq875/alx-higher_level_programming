#!/usr/bin/python3
"""Task 12"""


class MyInt(int):
    """This  class inherits from int"""
    def __init__(self, oosi):
        self.num = oosi

    def __eq__(self, oosi):
        """To make the equal to sign a rebel"""
        return self.num != oosi

    def __ne__(self, oosi):
        return self.num == oosi
