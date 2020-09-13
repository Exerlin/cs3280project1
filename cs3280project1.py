#!/usr/bin/env python3
'''
Main script that accepts user input and provides methods.
'''

import os
import sys
import re
import utils

card_type_file = open(os.path.join(sys.path[0], "credit_card_types.ssv"), "r")
card_type_info = card_type_file.read().split("\n")
array_of_string_arrays = []

def regex_check_for_errors(the_numbers):
    '''
    regex_check_for_errors(the_numbers) that returns a string
    Returns a string completely made out of digits if the given string
    passes regex checks. Returns "Invalid" otherwise.
    '''
    regex_string_16_digit = re.compile(r'^([0-9]{4}\D?){4}$')
    regex_string_13_15_digit = re.compile(r'^[0-9]{13,15}$')
    regex_string_17_19_digit = re.compile(r'^[0-9]{17,19}$')

    if regex_string_13_15_digit.search(the_numbers) is not None:
        return regex_string_13_15_digit.search(the_numbers).group()
    if regex_string_17_19_digit.search(the_numbers) is not None:
        return regex_string_17_19_digit.search(the_numbers).group()
    if regex_string_16_digit.search(the_numbers) is not None:
        return remove_nondigits(regex_string_16_digit.search(the_numbers).group())
    return "Invalid"

def remove_nondigits(the_string):
    '''
    remove_nondigits(the_string) that returns a string
    Returns the given string with all non-digits removed.
    '''
    regex_to_substitute = re.compile(r'\D')
    return regex_to_substitute.sub("", the_string)

def parse_ssv():
    '''
    parse_ssv() void
    Divides a string with values seperated by semicolons into an array, then
    divides each array with values seperated by commas into an array for
    further processing purposes
    '''
    for string_array in card_type_info:
        string_array = string_array.split(';')
        string_array[1] = string_array[1].split(',')
        string_array[2] = string_array[2].split(',')
        array_of_string_arrays.append(string_array)

def find_credit_card_type(the_int):
    '''
    find_credit_card_type(the_int) that returns a string
    Returns a string representing the credit card type.
    Returns "No Match" otherwise.
    '''
    for card_type_index in enumerate(array_of_string_arrays):
        if verify_match(the_int, int(card_type_index[0])):
            return array_of_string_arrays[int(card_type_index[0])][0]
    return "No Match"

def verify_match(the_int, card_type_index):
    '''
    verify_match(the_int, card_type_index) that returns True or False
    Calls match_card_type_length(the_int, card_type_index) and
    match_card_type_first_numbers(the_int, card_type_index)
    Returns True if both methods return True.
    Returns False otherwise.
    '''
    match_one = match_card_type_length(the_int, card_type_index)
    match_two = match_card_type_first_numbers(the_int, card_type_index)
    if match_one and match_two:
        return True
    return False

def match_card_type_length(the_int, index_of_type_to_test):
    '''
    match_card_type_length(the_int, index_of_type_to_test) that returns True or False
    Returns True if the_int's length matches the credit card type being tested.
    Returns False otherwise.
    '''
    type_to_test_array = array_of_string_arrays[index_of_type_to_test]

    for current_index in type_to_test_array[1]:
        if int(current_index) == len(str(the_int)):
            return True
    return False

def match_card_type_first_numbers(the_int, index_of_type_to_test):
    '''
    match_card_type_first_numbers(the_int, index_of_type_to_test) that returns True or False
    Returns True if the first numbers in the_int match the first numbers in
    the credit card type being tests.
    Returns False otherwise.
    '''
    type_to_test_array = array_of_string_arrays[index_of_type_to_test]

    for current_index in type_to_test_array[2]:
        try:
            if int(current_index) == int(str(the_int)[0: len(current_index): 1]):
                return True
        except ValueError:
            range_array = current_index.split('-')
            temp_int = int(str(the_int)[0: len(current_index): 1])
            if int(range_array[0]) <= temp_int <= int(range_array[1]):
                return True
    return False

def print_credit_card_results(number):
    '''
    print_credit_card_results(number) void
    Calls the methods to determine a credit card number's type and validity.
    Prints the results to the console in a readable format.
    '''
    print("Credit card number: " + number)
    print("Credit card type: " + find_credit_card_type(number))
    print("Luhn verification: " + utils.luhn_verified(number))

def get_input(prompt):
    '''
    get_input(prompt) that returns a string
    Prints prompt to console and returns the user's next input.
    '''
    print(prompt)
    return input()

def main():
    '''
    Launch method
    '''
    parse_ssv()
    while True:
        number = get_input('Please enter a credit card number:')
        number = (regex_check_for_errors(number))
        if utils.is_valid(number):
            print_credit_card_results(number)

if __name__ == "__main__":
    main()
