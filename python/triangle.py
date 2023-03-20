"""Determine if a triangle fulfill equilateral, isosceles, or scalene
by inputting list of lengths"""

def equilateral(sides):
    """
    Determine if a list of three sides can create equilateral type of triangle

    :param sides: list - integer number of triangle sides
    :return bool - is Equilateral true or false
    """
    if check(sides) and (sides[0] == sides[1] == sides[2]):
        return True
    return False

def isosceles(sides):
    """
    Determine if a list of three sides can create isoceles type of triangle

    :param sides: list - integer number of triangle sides
    :return bool - is Isoceles true or false
    """
    if check(sides) and\
        ((sides[0] == sides[1]) or\
        (sides[0] == sides[2]) or\
        (sides[1] == sides[2])):
        return True
    return False

def scalene(sides):
    """
    Determine if a list of three sides can create scalene type of triangle

    :param sides: list - integer number of triangle sides
    :return bool - is Scalene true or false
    """
    if check(sides) and \
        ((sides[0] != sides[1]) and\
         (sides[0] != sides[2]) and\
         (sides[1] != sides[2])):
        return True
    return False

def check(sides):
    """
    Check is the number fulfill the requirement of a triangle. 
    By more than 0 and sum of two sides more than or equal a side

    :param sides: list - integer number of triangle sides
    :return bool - is fulfill the requirement of triangle
    """
    if (sides[0] and sides[1] and sides[2]) > 0 and\
        (sides[0] + sides[1] >= sides[2]) and\
        (sides[0] + sides[2] >= sides[1]) and\
        (sides[1] + sides[2] >= sides[0]):
        return True
    return False
