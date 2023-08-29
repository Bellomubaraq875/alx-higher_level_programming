#!/usr/bin/python3
"""This is a class node that defines
a node of a singly linked list
"""


class Node:
    def __init__(self, data, next_node=None):
        """This is to initialize
        tje data for thwe node
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """This is to set the getter"""
        return self.__data

    @data.setter
    def data(self, value):
        """This checks if the type of the data is int
        and raises an error if it isn't
        """
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """This retrieves the data of the next node
        and makes sure it is a private attribute
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """This checks if the value is a node
        or none, and raises an error Appropriately
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """This is to create the actual singly linked list"""
    def __init__(self):
        """Create a private instance attribute"""
        self.head = None

    def __str__(self):
        """This returns the string to print"""
        return self.print_list()

    def sorted_insert(self, value):
        """This inserts a new node
        into the correct sorted position in increasing order in the list
        """
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            return
        elif value <= self.head.data:
            newNode.next_node = self.head
            self.head = newNode
            return

        present = self.head
        while present.next_node is not None and value > present.next_node.data:
            present = present.next_node
        newNode.next_node = present.next_node
        present.next_node = newNode

    def print_list(self):
        """This is to print
        the list of nodes one by one
        """
        string = ''
        present = self.head
        while present.next_node is not None:
            string += (str(present.data) + '\n')
            present = present.next_node
        string += str(present.data)
        return string
