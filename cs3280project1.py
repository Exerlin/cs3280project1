#!/usr/bin/env python3

import re
import utils
import os
import sys

card_type_file = open(os.path.join(sys.path[0], "credit_card_types.ssv"), "r")
card_type_info = card_type_file.read().split("\n")
array_of_string_arrays = []

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

def parse_ssv():
    for string_array in card_type_info:
        string_array = string_array.split(';')
        string_array[1] = string_array[1].split(',')
        string_array[2] = string_array[2].split(',')
        print(str(string_array[0]) + str(string_array[1]) + str(string_array[2]))
        array_of_string_arrays.append(string_array)
        
    
def find_credit_card_type(the_int):
    for card_type_index in range(len(array_of_string_arrays)):
        if(match_card_type_length(the_int, card_type_index) and match_card_type_first_numbers(the_int, card_type_index)):
            return array_of_string_arrays[card_type_index][0]
    return "No Match"
    

def match_card_type_length(the_int, index_of_type_to_test):
        
    type_to_test_array = array_of_string_arrays[index_of_type_to_test]

    for current_index in type_to_test_array[1]:
        if(int(current_index) == len(str(the_int))):
            return True
    return False

def match_card_type_first_numbers(the_int, index_of_type_to_test):
    
    type_to_test_array = array_of_string_arrays[index_of_type_to_test]

    for current_index in type_to_test_array[2]:
        try:
            if(int(current_index) == int(str(the_int)[0: len(current_index): 1])):
                return True
        except:
            range_array = current_index.split('-')
            temp_int = int(str(the_int)[0: len(current_index): 1])
            if(int(range_array[0]) <= temp_int and int(range_array[1]) >= temp_int):
                return True
            
    return False

def print_credit_card_results(number):
    print("Credit card number: " + number)
    print("Credit card type: " + find_credit_card_type(number))
    print("Luhn verification: " + utils.luhn_verified(number))

def get_input(prompt):
    print(prompt)
    return input()

def main():
    parse_ssv()
    while True:
        number = get_input('Please enter a credit card number:')
        number = (regex_check_for_errors(number))
        if(utils.is_valid(number)):
            print_credit_card_results(number)

if __name__ == "__main__":
    main()

