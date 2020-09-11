#!/usr/bin/env python3

'''
    luhn_verified(credit_card_number) that returns the string
    “Authentic” if the card is real or “Fake” if the specified
    credit_card_number is not genuine.
'''
def luhn_verified(int_array):
    for index in range(len(int_array)):
        if(index % 2 == 1):
            int_array[index] = int_array[index] * 2
        if(int_array[index] > 9):
            int_array[index] = int_array[index] - 9

    sum_of_all_numbers = 0
    
    for current_int in int_array:
        sum_of_all_numbers += current_int

    if(((sum_of_all_numbers * 9) % 10) == 0):
        return "Authentic" + str(sum_of_all_numbers)
    else:
        return "Fake" + str(sum_of_all_numbers)
        
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
    
