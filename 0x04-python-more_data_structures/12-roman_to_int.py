#!/usr/bin/python3
def roman_to_int(roman_string):
    roman_dict = {'I': 1, 'V': 5, 'X': 10,
                  'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    number = 0
    i = 0
    if roman_string and isinstance(roman_string, str):
        while i < len(roman_string) - 1:
            if roman_dict[roman_string[i]] >= roman_dict[roman_string[i + 1]]:
                number += roman_dict[roman_string[i]]
            else:
                number -= roman_dict[roman_string[i]]
            i += 1
        number += roman_dict[roman_string[i]]
        return number
    return 0
