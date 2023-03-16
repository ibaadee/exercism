"""Counting difference of squares between number"""

def square_of_sum(number):
    """Square number of the sum of first natural number

    param: number: int - last natural number
    return: int - square of sum of first natural number
    """
    number_sum = 0
    for index in range(1, number+1):
        number_sum += index
    return pow(number_sum, 2)


def sum_of_squares(number):
    """Sum of square of the first natural number
    
    param: number: int - last natural number
    return: int - sum of squares from n natural number
    """
    number_sum = 0
    for index in range(1, number+1):
        number_sum += pow(index,2)
    return number_sum


def difference_of_squares(number):
    """difference between squares

    param: number: int - last natural number
    return: substraction of square of sum and sum of square based on last
    natural number
    """
    return square_of_sum(number) - sum_of_squares(number)
