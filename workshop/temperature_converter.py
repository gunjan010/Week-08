def f_to_c(f):
    '''Convert argument temperature from fahrenheit to celsius.'''
    if (isinstance(f, int) or isinstance(f, float)):
        return (f-32)*(5/9)
    else:
        raise TypeError("Only int or float is allowed.")
    
def c_to_fc(c):
    # checking if c is int or a float otherwise raising a TypeError
    if not isinstance(c, (int, float)):
        raise TypeError("The value can be only int or float.")
    return (9/5 * c) + 32