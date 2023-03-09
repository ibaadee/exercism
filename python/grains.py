def square(number):
    grainNumber = pow(2, number - 1)
        
    if 0 < number <= 64: 
        return grainNumber
    else:
        raise ValueError("square must be between 1 and 64")

def total():
    totalGrains = 0
    for x in range(64):
        totalGrains += pow(2, x)
    return totalGrains
