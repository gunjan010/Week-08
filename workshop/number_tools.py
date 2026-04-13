def is_even(n):
    '''Return True if n is an even integer, otherwise False.'''
    if isinstance(n, int):
        return n % 2 == 0
    else:
        raise TypeError("Only int is allowed.")
    
def average(numbers):
    '''Checks if the passed argument is list, not empty, and every item is int/float 
       and raises Error if not. Returns the average of items in the list. '''
    total = 0
    if not isinstance(numbers, list):
        raise TypeError("Argument must be a list.")
    if len(numbers) == 0:
        raise ValueError("List must not be empty.")
    for number in numbers:
        if not isinstance(number, (int, float)):
            raise TypeError("All items must be int or float.")
        total += number
    return total / len(numbers)