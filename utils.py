#!/usr/bin/env python3
'''
Module that provides verification methods.
'''

def luhn_verified(credit_card_number):
    '''
    luhn_verified(credit_card_number) that returns a string
    Returns “Authentic” if the card is real or
    “Fake” if the specified credit_card_number is not genuine.
    '''
    sum_of_all_numbers = 0

    int_array = [int(x) for x in str(credit_card_number)]

    for index in range(len(int_array) - 1):
        if index % 2 == len(int_array) % 2:
            int_array[index] = int_array[index] * 2
        if int_array[index] > 9:
            int_array[index] = int_array[index] - 9
        sum_of_all_numbers += int_array[index]

    if ((sum_of_all_numbers % 10) + int_array[len(int_array) - 1]) == 10:
        return "Authentic"
    return "Fake"

def is_valid(sequence):
    '''
    is_valid(sequence) that returns true
    if the specified string sequence is a valid credit card number,
    return true and false otherwise.
    '''
    try:
        sequence = int(sequence)
        return True
    except ValueError:
        print('Please enter a valid credit card number.')
        return False
