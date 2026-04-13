def is_even(n):
    '''Return True if n is an even integer, otherwise False.'''
    if isinstance(n, int):
        return n % 2 == 0
    else:
        raise TypeError("Only int is allowed.")