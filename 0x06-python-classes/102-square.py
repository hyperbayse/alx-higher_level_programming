#!/usr/bin/python3
""" This module defines a class -Square- with
the neccessary attributes """


class Square:
    """ a class with  private attribute -size-
     and public method -area- """
    def __init__(self, size=0):
        """ validation of size value, if it is less
        than 0 a value eror is raised and must be
        an integer """
        if (type(size) is not int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """ returns the square area """
        return (self.__size ** 2)

    @property
    def size(self):
        """ retrieve the size value """
        return self.__size

    @size.setter
    def size(self, value):
        """ sets value for size attribute """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def __eq__(self, other):
        """ define the += comparison """
        return self.__size == other.size

    def __ne__(self, other):
        """ define the != comparison """
        return self.__size != other.size

    def __gt__(self, other):
        """ define the > comparison """
        return self.__size > other.size

    def __ge__(self, other):
        """ define the >= comparison """
        return self.__size >= other.size

    def __lt__(self, other):
        """ define the < comparison """
        return self.__size < other.size

    def __le__(self, other):
        """ define the <= comparison """
        return self.__size <= other.size