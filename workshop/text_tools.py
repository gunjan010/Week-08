def count_vowels(text):
    '''Return the number of vowels in a string.'''
    if not isinstance(text, str):
        raise TypeError("Argument must be a string.")

    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1

    return count