#!/usr/bin/env python3

import re
import utils

def int_to_array(the_int):
    return [int(x) for x in str(the_int)]

def regex_check_for_errors(the_numbers):
    regex_string_16_digit = re.compile(r'^([0-9]{4}\D?){4}$')
    regex_string_13_15_digit = re.compile(r'^[0-9]{13,15}$')
    regex_string_17_19_digit = re.compile(r'^[0-9]{17,19}$')

    if(regex_string_13_15_digit.search(the_numbers) is not None):
        return regex_string_13_15_digit.search(the_numbers).group()
    if(regex_string_17_19_digit.search(the_numbers) is not None):
        return regex_string_17_19_digit.search(the_numbers).group()
    if(regex_string_16_digit.search(the_numbers) is not None):
        return remove_nondigits(regex_string_16_digit.search(the_numbers).group())
    return "Invalid"

def remove_nondigits(the_string):
    regex_to_substitute = re.compile(r'\D')
    return regex_to_substitute.sub("", the_string)

while True:
    print('Please enter a credit card number:')
    number = input()
    number = (regex_check_for_errors(number))
    if(utils.is_valid(number)):
        print("Credit card number: " + number)
        print("Credit card type: ")
        print("Luhn verification: " + utils.luhn_verified(int_to_array(number)))

