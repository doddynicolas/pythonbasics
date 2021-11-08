def roman_to_int(input):
    try: input = input.upper(  )
    except AttributeError:
        raise TypeError, 'expected string, got %s' % type(input)
    # map of (numeral, value, maxcount) tuples
    roman_numeral_map = (('M', 1000, 3), ('CM', 900, 1),
        ('D', 500, 1), ('CD', 400, 1),
        ('C', 100, 3), ('XC', 90, 1),
        ('L', 50, 1), ('XL', 40, 1),
        ('X', 10, 3), ('IX', 9, 1),
        ('V', 5, 1), ('IV', 4, 1), ('I', 1, 3))
    result, index = 0, 0
    for numeral, value, maxcount in roman_numeral_map:
        count = 0
        while input[index: index+len(numeral)] == numeral:
            count += 1 # how many of this numeral we have
            if count > maxcount:
                raise ValueError, \
                    'input is not a valid roman numeral: %s' % input
            result += value
            index += len(numeral)
    if index < len(input): # There are characters unaccounted for
        raise ValueError, 'input is not a valid roman numeral: %s'%input
    return result