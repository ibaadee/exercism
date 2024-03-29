""""Counting leap year with conditions"""

def leap_year(year):
    """Counting leap year

    The conditions: 
    on every year that is evenly divisible by 4
    except every year that is evenly divisible by 100
    unless the year is also evenly divisible by 400
    
    param: year: int - input year
    return: boolean - is input year leap year or not
    """
    if year % 4 == 0:
        if year % 100 != 0:
            return True
        if year % 400 == 0:
            return True
    return False
