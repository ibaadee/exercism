def is_armstrong_number(number):
    number_string = str(number)
    number_length = len(number_string)
    
    armstrong_number_counter = 0
    for x in range(0, number_length):
        armstrong_number_counter += pow(int(number_string[x]), number_length)

    if number == armstrong_number_counter:
        return True
    else:
        return False

    
