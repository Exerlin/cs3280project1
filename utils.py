#!/usr/bin/env python3

'''
    luhn_verified(credit_card_number) that returns the string
    “Authentic” if the card is real or “Fake” if the specified
    credit_card_number is not genuine.
'''
def luhn_verified(int_array):
    sum_of_all_numbers = 0
    
    for index in range(len(int_array) - 1):
        if(index % 2 == len(int_array) % 2):
            int_array[index] = int_array[index] * 2
        if(int_array[index] > 9):
            int_array[index] = int_array[index] - 9
        sum_of_all_numbers += int_array[index]

    if(((sum_of_all_numbers % 10) + int_array[len(int_array) - 1]) == 10):
        return "Authentic"
    else:
        return "Fake"

'''
    is_valid(sequence) that returns true
    if the specified string sequence is in a valid credit card number format,
    and false otherwise.
'''
def is_valid(sequence):
    try:
        sequence = int(sequence)
        return True
    except:
        print('Please enter a valid credit card number.')
        return False
    
