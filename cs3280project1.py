#!/usr/bin/env python3

# module at ..\python\utils.py
import re



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

print(regex_check_for_errors("1234567890123"))
print(regex_check_for_errors("1234567890123456"))
print(regex_check_for_errors("1234 5678 9012 3456"))
print(regex_check_for_errors("1234-5678-9012-3456"))
print(regex_check_for_errors("123456789012345678"))
print(regex_check_for_errors("1234567890123456789"))

print(regex_check_for_errors("12345678901234567890"))
print(regex_check_for_errors("1234  5678  9012  3456"))
print(regex_check_for_errors("1234 56789012345678"))
